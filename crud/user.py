from sqlalchemy.orm import Session
from models.user import User
from schema.user import UserCreate
from . import organization as crud_org # Importante añadir esto

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user: UserCreate):
    fake_hashed = user.password + "notreallyhashed"
    db_user = User(
        email=user.email,
        full_name=user.full_name,
        hashed_password=fake_hashed,
        address_id=user.address_id
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(User).offset(skip).limit(limit).all()

# --- NUEVA FUNCIÓN ---
def add_organization_to_user(db: Session, user_id: int, org_id: int):
    user = get_user(db, user_id=user_id)
    # Se necesita la función get_organization, la importamos con un alias
    organization = crud_org.get_organization(db, org_id=org_id)
    
    if not user or not organization:
        return None
    
    user.organizations.append(organization)
    db.commit()
    db.refresh(user)
    return user