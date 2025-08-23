import socket
from typing import Optional
from sqlalchemy.orm import Session
from models.server import Server
from schema.server import ServerCreate, ServerUpdate

def create_server(db: Session, server: ServerCreate):
    db_server = Server(**server.dict())
    db.add(db_server)
    db.commit()
    db.refresh(db_server)
    return db_server

def get_servers(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Server).offset(skip).limit(limit).all()

def get_server(db: Session, server_id: int):
    return db.query(Server).filter(Server.id == server_id).first()

def update_server(db: Session, server_id: int, server: ServerUpdate):
    db_server = db.query(Server).filter(Server.id == server_id).first()
    if db_server:
        for key, value in server.dict().items():
            setattr(db_server, key, value)
        db.commit()
        db.refresh(db_server)
    return db_server

def delete_server(db: Session, server_id: int):
    db_server = db.query(Server).filter(Server.id == server_id).first()
    if db_server:
        db.delete(db_server)
        db.commit()
    return db_server

def check_server_status(ip_address: str, port: Optional[int]) -> str:
    """Verifica si un puerto está abierto en una IP. Devuelve 'active' o 'inactive'."""
    if not port:
        return "unknown"  # No podemos verificar si no hay puerto
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(3)  # Timeout de 3 segundos
    
    try:
        # connect_ex devuelve 0 si la conexión es exitosa
        if sock.connect_ex((ip_address, port)) == 0:
            return "active"
        else:
            return "inactive"
    except (socket.gaierror, socket.error):
        # Error de resolución de nombre o de conexión
        return "inactive"
    finally:
        sock.close()