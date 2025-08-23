from pydantic import BaseModel
from typing import List, Optional

class ServerBase(BaseModel):
    name: str
    ip_address: str
    status: str
    organization_id: int
    port: Optional[int] = None

class ServerCreate(ServerBase):
    pass

class ServerUpdate(ServerBase):
    pass

class Server(ServerBase):
    id: int

    class Config:
        orm_mode = True
