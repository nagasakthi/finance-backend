from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models import Record
from dependencies import get_db, require_role

router = APIRouter(prefix="/dashboard")

@router.get("/")
def get_summary(
    db: Session = Depends(get_db),
    user=Depends(require_role(["admin", "analyst"]))
):
    records = db.query(Record).all()

    income = sum(r.amount for r in records if r.type == "income")
    expense = sum(r.amount for r in records if r.type == "expense")

    return {
        "total_income": income,
        "total_expense": expense,
        "net_balance": income - expense
    }