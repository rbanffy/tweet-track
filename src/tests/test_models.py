"Tests the models package"

import unittest

from models import Entity


class TestEntity(unittest.TestCase):
    "An Entity controls one or more accounts in one or mode service"

    def setUp(self):
        e = Entity(name="Entity 1", description="Entity 1's description")
        self.assertIsNone(e.key)
        self.key = e.save()

    def test_create_entity(self):
        e = Entity(name="Entity 2", description="Entity 2's description")
        self.assertIsNone(e.key)
        e.save()
        self.assertIsNotNone(e.key)
        self.assertEqual(e.name, "Entity 2")
        self.assertEqual(e.description, "Entity 2's description")

    def test_get_entity_by_name(self):
        e = Entity.get_by_name("Entity 1")
        self.assertEqual(e.description, "Entity 1's description")

    def test_get_entity_by_key(self):
        e = Entity.get_by_key(self.key)
        self.assertEqual(e.name, "Entity 1")
        self.assertEqual(e.description, "Entity 1's description")
