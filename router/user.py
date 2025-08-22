from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crud import user as user_crud
from schema.user import User, UserCreate
from db.database import get_db

router = APIRouter()

@router.post("/users/", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = user_crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return user_crud.create_user(db, user)

@router.get("/users/", response_model=list[User])
def list_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return user_crud.get_users(db, skip=skip, limit=limit)

@router.get("/users/{user_id}", response_model=User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = user_crud.get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.get("/users/email/{email}", response_model=User)
def read_user_by_email(email: str, db: Session = Depends(get_db)):
    db_user = user_crud.get_user_by_email(db, email=email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# --- NUEVO ENDPOINT ---
@router.post("/users/{user_id}/organizations/{organization_id}", response_model=User)
def add_organization_to_user_endpoint(user_id: int, organization_id: int, db: Session = Depends(get_db)):
    db_user = user_crud.add_organization_to_user(db, user_id=user_id, org_id=organization_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User or Organization not found")
    return db_user
