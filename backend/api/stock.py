from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.core.db import get_db
from backend.models.models import Product
from backend.services.product_service import get_stock_warn

router = APIRouter(prefix="/stock", tags=["库存管理"])

@router.put("/update")
def update_stock(id: int, stock: int, db: Session = Depends(get_db)):
    db.query(Product).filter(Product.id == id).update({"stock": stock})
    db.commit()
    return {"msg": "库存更新成功"}

@router.get("/warn")
def stock_warn(db: Session = Depends(get_db)):
    return get_stock_warn(db)