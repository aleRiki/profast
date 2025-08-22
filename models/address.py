from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String
from db.database import Base

class Address(Base):
    __tablename__ = "addresses"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    street: Mapped[str] = mapped_column(String(100))

    users: Mapped[list["User"]] = relationship(back_populates="address")
    organizations: Mapped[list["Organization"]] = relationship(back_populates="address")
