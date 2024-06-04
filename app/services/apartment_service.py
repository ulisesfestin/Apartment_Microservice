from app.models import Apartment
from app.repositories import ApartmentRepository
from app import cache

apartment_repository = ApartmentRepository()

class ApartmentService:

    def create(self, entity: Apartment) -> Apartment:
        apartment = apartment_repository.create(entity)
        cache.set(f'{apartment.id}', apartment, timeout=50)
        return apartment
    
    def update(self, entity: Apartment, id: int) -> Apartment:
        apartment = cache.get(f'{id}')
        if apartment:
            cache.update(f'{apartment.id}', entity, timeout=50)
            apartment = apartment_repository.update(entity, id)
        else:
            apartment = apartment_repository.update(entity, id)
            cache.set(f'{apartment.id}', apartment, timeout=50)
        return apartment
    
    def find_by_id(self, id: int) -> Apartment:
        apartment = cache.get(f'{id}')
        if apartment is None:
            apartment = apartment_repository.find_by_id(id)
            if not apartment:
                return None
            cache.set(f'{apartment.id}', apartment, timeout=50)
        return apartment
    
    @cache.memoize(timeout=50)
    def find_all(self) -> list:
        return apartment_repository.find_all()
    
    def delete(self, id: int) -> Apartment:
        apartment = cache.get(f'{id}')
        if apartment:
            cache.delete(f'{apartment.id}')
        return apartment_repository.delete(id)
    
    def search(self, lease_min: str, lease_max: str) -> list:
        return apartment_repository.search(lease_min, lease_max)
    
    
