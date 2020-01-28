"""
# Models

Models using the Google Firestore in Native mode.
"""

import datetime


class Entity:
    def __init__(self, name, description=""):
        self.name = name
        self.description = description
        self.key = None

    def save(self):
        # TODO: Actually save
        self.key = "TEYUItyu3y"
        return self.key

    @classmethod
    def get_by_name(cls, name):
        # TODO: Get something
        e = Entity(name="Entity 1", description="Entity 1's description")
        e.key = "TEYUItyu3y"
        return e

    @classmethod
    def get_by_key(cls, key):
        # TODO: Get something
        e = Entity(name="Entity 1", description="Entity 1's description")
        e.key = "TEYUItyu3y"
        return e

    def get_service_accounts(self):
        "Returns all service accounts of this entity"
        # TODO: Get the accounts
        return []


class Account:
    def __init__(self, service_name, service_id=None):
        self.service_name = service_name
        # This is the id within a given service.
        self.service_id = service_id
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        # key is populated on save.
        self.key = None
        # Screen names is a list of (timestamp, screen_name) across
        # multiple updates of the record.
        self.screen_names = []
        # TODO: At the end of the __init__ mark this for updating by
        # scheduling an update job for this service and id.

    def save(self):
        # TODO: Actually save
        self.key = "TEYUItyu3y"
        return self.key

    @classmethod
    def get_by_service_and_id(cls, service, service_id):
        # TODO: Get something
        ...

    @classmethod
    def get_by_key(cls, key):
        # TODO: Get something
        ...

    def update(self):
        "Calls the service APIs to update its data."
        # TODO: Update the data.
        ...
