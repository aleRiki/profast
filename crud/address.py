from sqlalchemy.orm import Session
from models.address import Address
from schema.address import AddressCreate

def create_address(db: Session, address: AddressCreate):
    db_address = Address(**address.dict())
    db.add(db_address)
    db.commit()
    db.refresh(db_address)
    return db_address

def get_address(db: Session, address_id: int):
    return db.query(Address).filter(Address.id == address_id).first()

def get_addresses(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Address).offset(skip).limit(limit).all()