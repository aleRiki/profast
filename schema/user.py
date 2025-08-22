from pydantic import BaseModel
from typing import List, Optional
from .address import Address
from .organization import Organization

class UserBase(BaseModel):
    email: str
    full_name: str

class UserCreate(UserBase):
    password: str
    address_id: int

class User(UserBase):
    id: int
    address: Optional[Address] = None
    organizations: List[Organization] = []

    class Config:
        orm_mode = True
