from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud import server as server_crud
from schema.server import Server, ServerCreate, ServerUpdate
from schema.user import User
from auth.dependencies import get_current_user
from db.database import get_db

router = APIRouter(prefix="/servers", tags=["servers"])

@router.post("/", response_model=Server)
def create_server(server: ServerCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return server_crud.create_server(db=db, server=server)

@router.get("/", response_model=list[Server])
def read_servers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return server_crud.get_servers(db=db, skip=skip, limit=limit)

@router.get("/{server_id}", response_model=Server)
def read_server(server_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_server = server_crud.get_server(db=db, server_id=server_id)
    if db_server is None:
        raise HTTPException(status_code=404, detail="Server not found")
    return db_server

@router.put("/{server_id}", response_model=Server)
def update_server(server_id: int, server: ServerUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_server = server_crud.update_server(db=db, server_id=server_id, server=server)
    if db_server is None:
        raise HTTPException(status_code=404, detail="Server not found")
    return db_server

@router.delete("/{server_id}", response_model=Server)
def delete_server(server_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_server = server_crud.delete_server(db=db, server_id=server_id)
    if db_server is None:
        raise HTTPException(status_code=404, detail="Server not found")
    return db_server

@router.post("/{server_id}/ping/", response_model=Server)
def ping_server(server_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_server = server_crud.get_server(db, server_id=server_id)
    if not db_server:
        raise HTTPException(status_code=404, detail="Server not found")
    
    status = server_crud.check_server_status(db_server.ip_address, db_server.port)
    
    db_server.status = status
    db.commit()
    db.refresh(db_server)
    
    return db_server
