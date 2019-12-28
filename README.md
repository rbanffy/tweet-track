# Tweet-track
A tool for tracking people on Twitter and Gab. Runs on Google App Engine
(https://cloud.google.com/appengine/)

# API endpoints

- `GET /v1/{service}/id/{id}/info.json`

  Returns the information we have on this specific user of the service
  (includes past and current `screen_name`s)

- `GET /v1/{service}/screen_name/{screen_name}/info.json`

  Returns the information we have on this service's `screen_name`.

- `GET /v1/person/{id}/info.json`

  Returns the information we have on this person, from all connected
  services.

# Models

                           1 +------+
                     |-------|Person|
                     |       +------+
                     | n
                 +---+---+ 1         n +-------+
                 |Account|-------------|Profile|
                 +-------+             +-------+

# Background tasks

All accounts are checked for changes in metadata. New data is added to
new profile entities and tied to that unique identity. Timelines are
captured and stored in buckets named /{account}/{timestamp} and the path
is noted on the Profile entity. Base paths are stored in the config.py
file and secrets are in the secrets.py file, which is not under source
control.
