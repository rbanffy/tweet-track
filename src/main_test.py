# Copyright 2018 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import http

import main


def test_root():
    main.app.testing = True
    client = main.app.test_client()

    r = client.get("/")
    assert r.status_code == http.HTTPStatus.NOT_FOUND


def test_person():
    main.app.testing = True
    client = main.app.test_client()

    r = client.get("/v1/person/1234/info.json")
    assert r.status_code == 200


def test_id_on_service():
    main.app.testing = True
    client = main.app.test_client()

    r = client.get("/v1/twitter/id/1234/info.json")
    assert r.status_code == 200
