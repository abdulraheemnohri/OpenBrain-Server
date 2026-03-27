import unittest
import sqlite3
import os
from backend.auth.api_keys import generate_api_key, get_all_api_keys
from backend.auth.security import validate_api_key
from backend.database.models import setup_models
from backend.core.router import AIRouter

class TestExpertAICore(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Set up a test database if needed or just use the default initialized one for basic unit tests
        # For simplicity, we assume setup_models() was called by main.py
        setup_models()

    def test_api_key_generation(self):
        key = generate_api_key(usage_limit=500)
        self.assertTrue(key.startswith("sk-"))
        self.assertTrue(validate_api_key(key))

    def test_router(self):
        router = AIRouter()
        self.assertEqual(router.route_query("Write a python script"), "coding")
        self.assertEqual(router.route_query("Solve 1 + 1"), "math")
        self.assertEqual(router.route_query("Hello world"), "general")

if __name__ == "__main__":
    unittest.main()
