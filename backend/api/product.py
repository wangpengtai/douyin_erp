from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.core.db import get_db
from backend.services import product_service
from pydantic import BaseModel

router = APIRouter(prefix="/product", tags=["产品管理"])

class ProductCreate(BaseModel):
    name: str
    type: str = "单品"
    cost_price: float = 0
    sale_price: float = 0
    stock: int = 0
    warn_stock: int = 5
    freight: float = 0
    vat_rate: float = 13
    ad_fee: float = 0
    platform_fee: float = 0

@router.post("/add")
def add_product(product: ProductCreate, db: Session = Depends(get_db)):
    return product_service.create_product(db, product)

@router.delete("/delete/{id}")
def del_product(id: int, db: Session = Depends(get_db)):
    return product_service.delete_product(db, id)

@router.post("/bind_combine")
def bind(combo_id: int, item_id: int, num: int, db: Session = Depends(get_db)):
    return product_service.bind_combine(db, combo_id, item_id, num)
# ========== 新增：获取所有产品列表接口 ==========
@router.get("/list")
def list_products(db: Session = Depends(get_db)):
    products = db.query(product_service.Product).all()
    # 把对象转成字典返回
    return [
        {
            "id": p.id,
            "name": p.name,
            "type": p.type,
            "cost_price": p.cost_price,
            "sale_price": p.sale_price,
            "stock": p.stock,
            "warn_stock": p.warn_stock
        }
        for p in products
    ]