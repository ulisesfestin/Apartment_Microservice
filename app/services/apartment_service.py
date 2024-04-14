from app.models import Apartment
from app.repositories import ApartmentRepository

apartment_repository = ApartmentRepository()

class ApartmentService:

    def create(self, entity: Apartment) -> Apartment:
        return apartment_repository.create(entity)
    
    def update(self, entity: Apartment, id: int) -> Apartment:
        return apartment_repository.update(entity, id)
    
    def find_by_id(self, id: int) -> Apartment:
        return apartment_repository.find_by_id(id)
    
    def find_all(self) -> list:
        return apartment_repository.find_all()
    
    def delete(self, id: int) -> Apartment:
        return apartment_repository.delete(id)
    
    def search(self, lease_min: str, lease_max: str) -> list:
        return apartment_repository.search(lease_min, lease_max)
    
    
