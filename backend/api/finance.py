from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.core.db import get_db
from backend.services import finance_service

router = APIRouter(prefix="/finance", tags=["财务税务"])

@router.get("/calc/{combo_id}")
def calc_profit(combo_id: int, db: Session = Depends(get_db)):
    return finance_service.calc_combo_profit(db, combo_id)

@router.get("/dashboard")
def dashboard(db: Session = Depends(get_db)):
    sales, profit, warn = finance_service.get_dashboard_data(db)
    return {"total_sales": sales, "total_profit": profit, "warn_count": warn}