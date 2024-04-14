from app.models import Apartment
from app import db
from app.repositories.repository_base import Create, Read, Update, Delete


class ApartmentRepository(Create, Read, Update, Delete):

    def create(self, entity: Apartment) -> Apartment:
        db.session.add(entity)
        db.session.commit()
        return entity
    
    def update(self, apartment: Apartment, id: int) -> Apartment:
        entity = self.find_by_id(id)
        entity.number_of_apartment = apartment.number_of_apartment
        entity.size = apartment.size
        entity.amount_rooms = apartment.amount_rooms
        entity.features = apartment.features
        entity.availability = apartment.availability
        entity.lease = apartment.lease
        entity.address = apartment.address
        db.session.add(entity)
        db.session.commit()
        return entity
    
    def find_by_id(self, id: int) -> Apartment:
        return Apartment.query.get(id)
    
    def find_all(self) -> list:
        return db.session.query(Apartment).all()
    
    def delete(self, id: int) -> Apartment:
        entity = self.find_by_id(id)
        db.session.delete(entity)
        db.session.commit()
        return entity
    
    def search(self, lease_min: str, lease_max: str) -> list:
        return db.session.query(Apartment).filter(Apartment.lease.between(lease_min, lease_max)).all()