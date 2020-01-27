"""
# Models

Models using the Google App Engine datastore APIs.
"""


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
    def __init__(self, service_name, screen_name=None, service_id=None):
        self.service_name = service_name
        self.screen_name = screen_name
        self.service_id = service_id
        self.key = None
