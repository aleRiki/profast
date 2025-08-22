from pydantic import BaseModel

class AddressBase(BaseModel):
    street: str

class AddressCreate(AddressBase):
    pass

class Address(AddressBase):
    id: int

    class Config:
        orm_mode = True
