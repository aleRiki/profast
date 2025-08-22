from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import SessionLocal
from crud import organization
from schema.organization import Organization, OrganizationCreate
from db.database import get_db


router = APIRouter(prefix="/organizations", tags=["organizations"])



@router.post("/", response_model=Organization)
def create_org(org_in: OrganizationCreate, db: Session = Depends(get_db)):
    return organization.create_organization(db=db, org=org_in)

@router.get("/{org_id}", response_model=Organization)
def read_org(org_id: int, db: Session = Depends(get_db)):
    db_org = organization.get_organization(db, org_id)
    if db_org is None:
        raise HTTPException(status_code=404, detail="Organization not found")
    return db_org

@router.get("/", response_model=list[Organization])
def list_orgs(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return organization.get_organizations(db, skip=skip, limit=limit)


@router.put("/{org_id}", response_model=Organization)
def update_org(org_id: int, org_in: OrganizationCreate, db: Session = Depends(get_db)):
    db_org = organization.put_organization(db, org_id, org_in)
    if db_org is None:
        raise HTTPException(status_code=404, detail="Organization not found")
    return db_org