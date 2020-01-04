from flask import Flask

import api_v1

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)
app.register_blueprint(api_v1.endpoints, url_prefix="/v1")


@app.route("/healthcheck")
def healthcheck():
    """Return a friendly HTTP greeting."""
    return "OK"


if __name__ == "__main__":
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host="127.0.0.1", port=8080, debug=True)
