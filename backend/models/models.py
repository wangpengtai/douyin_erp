from sqlalchemy import Column, Integer, String, Float, ForeignKey
from backend.core.db import Base

# 产品表（单品/组合品）
class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)  # 产品名称
    type = Column(String, default="单品")  # 单品/组合品
    cost_price = Column(Float, default=0)  # 原料成本
    sale_price = Column(Float, default=0)  # 售价
    stock = Column(Integer, default=0)  # 库存
    warn_stock = Column(Integer, default=5)  # 库存预警线
    # 全成本字段
    freight = Column(Float, default=0)  # 运费
    vat_rate = Column(Float, default=13)  # 增值税率(%)
    ad_fee = Column(Float, default=0)  # 投流费用
    platform_fee = Column(Float, default=0)  # 平台服务费

# 产品组合关联表（组合品 → 单品）
class ProductCombine(Base):
    __tablename__ = "product_combine"
    id = Column(Integer, primary_key=True, index=True)
    combo_id = Column(Integer, ForeignKey("products.id"))  # 组合品ID
    item_id = Column(Integer, ForeignKey("products.id"))  # 子单品ID
    item_num = Column(Integer, default=1)  # 子单品数量