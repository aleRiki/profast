from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import get_db
from crud import address
from schema.address import Address, AddressCreate

router = APIRouter(prefix="/addresses", tags=["addresses"])

@router.post("/", response_model=Address)
def create_address(address_in: AddressCreate, db: Session = Depends(get_db)):
    return address.create_address(db=db, address=address_in)

@router.get("/{address_id}", response_model=Address)
def read_address(address_id: int, db: Session = Depends(get_db)):
    db_address = address.get_address(db, address_id)
    if db_address is None:
        raise HTTPException(status_code=404, detail="Address not found")
    return db_address

@router.get("/", response_model=list[Address])
def list_addresses(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return address.get_addresses(db, skip=skip, limit=limit)
