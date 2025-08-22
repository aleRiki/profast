from sqlalchemy.orm import Session
from models.organization import Organization
from schema.organization import OrganizationCreate

def create_organization(db: Session, org: OrganizationCreate):
    db_org = Organization(**org.dict())
    db.add(db_org)
    db.commit()
    db.refresh(db_org)
    return db_org

def get_organization(db: Session, org_id: int):
    return db.query(Organization).filter(Organization.id == org_id).first()

def get_organizations(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Organization).offset(skip).limit(limit).all()

def put_organization(db: Session, org_id: int, org: OrganizationCreate):
    db_org = db.query(Organization).filter(Organization.id == org_id).first()
    if db_org:
        for key, value in org.dict().items():
            setattr(db_org, key, value)
        db.commit()
        db.refresh(db_org)
    return db_org