from sqlalchemy.orm import Session
from backend.models.models import Product, ProductCombine

# 新增产品
def create_product(db: Session, product):
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

# 删除产品
def delete_product(db: Session, product_id: int):
    db.query(Product).filter(Product.id == product_id).delete()
    db.query(ProductCombine).filter(ProductCombine.combo_id == product_id).delete()
    db.commit()
    return True

# 绑定组合产品
def bind_combine(db: Session, combo_id: int, item_id: int, num: int):
    combine = ProductCombine(combo_id=combo_id, item_id=item_id, item_num=num)
    db.add(combine)
    db.commit()
    return True

# 库存预警查询
def get_stock_warn(db: Session):
    return db.query(Product).filter(Product.stock <= Product.warn_stock).all()