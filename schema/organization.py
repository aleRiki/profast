from pydantic import BaseModel
from typing import List, Optional
from .address import Address

class OrganizationBase(BaseModel):
    name: str

class OrganizationCreate(OrganizationBase):
    address_id: int

class Organization(OrganizationBase):
    id: int
    address: Optional[Address] = None

    class Config:
        orm_mode = True
