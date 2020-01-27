import http
import unittest

import main


class TestWebAPI(unittest.TestCase):
    def setUp(self):
        main.app.testing = True
        self.client = main.app.test_client()

    def test_root(self):
        r = self.client.get("/")
        self.assertEqual(r.status_code, http.HTTPStatus.NOT_FOUND)

    def test_person(self):
        r = self.client.get("/v1/person/1234/info.json")
        self.assertEqual(r.status_code, 200)

    def test_id_on_service(self):
        r = self.client.get("/v1/twitter/id/1234/info.json")
        self.assertEqual(r.status_code, 200)
