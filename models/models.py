from typing import Annotated
from sqlmodel import Field, SQLModel, create_engine,select 


class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    email: str = Field(default=None, index=True)
    full_name: str = Field(default=None)
    hashed_password: str = Field(default=None)