import unittest
from app import app


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.create_app()
        self.app_context = self.app.app_context()
        