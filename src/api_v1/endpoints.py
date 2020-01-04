"""
# API endpoints

The API endpoints, /person, {service}/id/{id}, and
{service}/screen_name/{screen_name}
"""

import http

from flask import Blueprint, abort, jsonify, render_template
from jinja2 import TemplateNotFound

endpoints = Blueprint("person", __name__, template_folder="templates")


@endpoints.route("/person/<person_id>/info.json", methods=["GET"])
def person(person_id: int):
    "Get the perso data from the store and return it as JSON"

    return jsonify(
        {
            "person_id": person_id,
            "twitter_id": 1234,
            "latest_twitter_screen_name": "abc",
            "twitter_screen_names": {
                "2018-01-01": "bbbn",
                "2019-12-20": "abc",
            },
            "first_seen": "2018-01-01",
            "last_seen": "2019-19-20",
        }
    )
    # abort(http.HTTPStatus.NOT_FOUND)


@endpoints.route("/<service>/id/<user_id>/info.json", methods=["GET"])
def id_on_service(service, user_id):
    return jsonify(
        {
            "person_id": 1234,
            "twitter_id": user_id,
            "last_twitter_screen_name": "abc",
            "twitter_screen_names": {
                "2018-01-01": "bbbn",
                "2019-12-20": "abc",
            },
            "first_seen": "2018-01-01",
            "last_seen": "2019-19-20",
        }
    )
