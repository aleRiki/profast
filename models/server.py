from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey, Table, Column
from db.database import Base
from models.organization import Organization
from typing import Optional

class Server(Base):
    __tablename__ = "servers"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    ip_address: Mapped[str] = mapped_column(String(100), nullable=False)
    status: Mapped[str] = mapped_column(String(50), nullable=False)
    port: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    organization_id: Mapped[int] = mapped_column(ForeignKey("organizations.id"), nullable=False)

    organization: Mapped["Organization"] = relationship(back_populates="servers")
