import unittest
from app import create_app, db
from app.models import Apartment
from app.services import ApartmentService

apartment_service = ApartmentService()

class TestApartment(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
    
    def test_create_apartment(self):
        entity = self.create_entity()
        self.assertTrue(entity.id)

    def create_entity(self):
        entity = Apartment(number_of_apartment=1, size=100, amount_rooms=3, features="balcony", availability=True, lease=1000.0, address="123 Main St")
        apartment_service.create(entity)
        return entity
    
    def test_delete_apartment(self):
        entity = self.create_entity()
        apartment_service.delete(entity.id)
        self.assertFalse(Apartment.query.get(entity.id))
    
    def test_find_by_id_apartment(self):
        entity = self.create_entity()
        self.assertTrue(apartment_service.find_by_id(entity.id))
    
    def test_find_all_apartment(self):
        entity = self.create_entity()
        self.assertTrue(apartment_service.find_all())
    
    def test_update_apartment(self):
        entity = self.create_entity()
        entity.size = 200
        apartment_service.update(entity, entity.id)
        self.assertEqual(apartment_service.find_by_id(entity.id).size, 200)


if __name__ == '__main__':
    unittest.main()