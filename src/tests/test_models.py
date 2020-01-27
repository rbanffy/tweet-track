"Tests the models package"

import unittest

import models


class TestEntity(unittest.TestCase):
    "An Entity controls one or more accounts in one or mode service"

    def test_create_entity(self):
        e = Entity(
            name="Entity 1",
            description="Entity 1's description"
        )
        self.assertNull(e.key)
        self.key = e.save()
        self.assertNotNull(e.key)
        self.assertEqual(e.name, "Entity 1")
        self.assertEqual(e.description, "Entity 1's description")

    def test_get_entity_by_name(self):
        e = Entity.get_by_name('Entity 1')
        self.assertEqual(e.description, "Entity 1's description")

    def test_get_entity_by_id(self):
        e = Entity.get_by_id(self.key)
        self.assertEqual(e.description, "Entity 1's description")
