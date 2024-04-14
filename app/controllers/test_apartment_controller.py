import unittest
from app import create_app, db
from app.models import Apartment
from app.services import ApartmentService

apartment_service = ApartmentService()

class TestApartment(unittest.TestCase):
    # ... existing test cases ...

    def test_find_all_endpoint(self):
        with self.app.test_client() as client:
            response = client.get('/findall')
            data = response.get_json()

            self.assertEqual(response.status_code, 200)
            self.assertEqual(data['message'], 'Apartments found!')
            self.assertIn('apartments', data['data'])
            self.assertIsInstance(data['data']['apartments'], list)

if __name__ == '__main__':
    unittest.main()