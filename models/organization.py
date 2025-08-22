from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey, Table, Column
from db.database import Base

# Tabla intermedia para Many-to-Many entre users y organizations
user_organization = Table(
    "user_organization",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("organization_id", Integer, ForeignKey("organizations.id"))
)

class Organization(Base):
    __tablename__ = "organizations"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))

    # relación muchos-a-muchos con User
    users: Mapped[list["User"]] = relationship(
        secondary=user_organization, back_populates="organizations"
    )

    # relación muchos-a-uno con Address
    address_id: Mapped[int] = mapped_column(ForeignKey("addresses.id"))
    address: Mapped["Address"] = relationship(back_populates="organizations")
