import unittest
from app import create_app, db, cache
import requests


class TestRequestsApartment(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        cache.init_app(self.app, config={'CACHE_TYPE': 'RedisCache', 'CACHE_DEFAULT_TIMEOUT': 300, 'CACHE_REDIS_HOST': 'localhost', 'CACHE_REDIS_PORT': '6379', 'CACHE_REDIS_DB': '0', 'CACHE_REDIS_PASSWORD': '12345', 'CACHE_KEY_PREFIX': 'apartment_'})
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        cache.clear()
        self.app_context.pop()
    
    def create_apartment(self):
        requests.post('http://localhost:5000/api/v1/apartment/create', json={
            "number_of_apartment": 1,
            "size": 50,
            "amount_rooms": 2,
            "features": "balcony",
            "availability": True,
            "lease": 1000,
            "address": "123 Main St"
        })

    def test_index(self):
        response = requests.get('http://localhost:5000/api/v1/apartment/')
        self.assertEqual(response.status_code, 200)
    
    def test_create(self):
        response = requests.post('http://localhost:5000/api/v1/apartment/create', json={
            "number_of_apartment": 1,
            "size": 50,
            "amount_rooms": 2,
            "features": "balcony",
            "availability": True,
            "lease": 1000,
            "address": "123 Main St"
        })
        self.assertEqual(response.status_code, 200)
    
    def test_update(self):
        self.create_apartment()
        response = requests.put('http://localhost:5000/api/v1/apartment/update/1', json={
            "number_of_apartment": 1,
            "size": 50,
            "amount_rooms": 2,
            "features": "balcony",
            "availability": False,
            "lease": 1000,
            "address": "123 Main St"
        })
        self.assertEqual(response.status_code, 200)

    def test_find_by_id(self):
        self.create_apartment()
        response = requests.get('http://localhost:5000/api/v1/apartment/findbyid/1')
        self.assertEqual(response.status_code, 200)
    
    def test_find_all(self):
        self.create_apartment()
        response = requests.get('http://localhost:5000/api/v1/apartment/findall')
        self.assertEqual(response.status_code, 200)
    
    def test_delete(self):
        self.create_apartment()
        response = requests.delete('http://localhost:5000/api/v1/apartment/delete/1')
        self.assertEqual(response.status_code, 200)
    
    def test_search(self):
        self.create_apartment()
        response = requests.get('http://localhost:5000/api/v1/apartment/search?lease_min=1000&lease_max=2000')
        self.assertEqual(response.status_code, 200)
    