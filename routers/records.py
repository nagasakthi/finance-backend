from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import crud, schemas
from dependencies import get_db, require_role

router = APIRouter(prefix="/records")

@router.post("/")
def create_record(
    record: schemas.RecordCreate,
    db: Session = Depends(get_db),
    user=Depends(require_role(["admin"]))
):
    return crud.create_record(db, record)

@router.get("/")
def get_records(
    db: Session = Depends(get_db),
    user=Depends(require_role(["admin", "analyst", "viewer"]))
):
    return crud.get_records(db)