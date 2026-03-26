from sqlalchemy.orm import Session
from backend.models.models import Product, ProductCombine

# 计算组合产品全成本+利润（核心功能）
def calc_combo_profit(db: Session, combo_id: int):
    # 1. 计算原料总成本
    items = db.query(ProductCombine).filter(ProductCombine.combo_id == combo_id).all()
    material_cost = 0
    for item in items:
        product = db.query(Product).filter(Product.id == item.item_id).first()
        material_cost += product.cost_price * item.item_num

    # 2. 获取组合品附加成本
    combo = db.query(Product).filter(Product.id == combo_id).first()
    freight = combo.freight
    vat = combo.sale_price * (combo.vat_rate / 100)  # 增值税
    ad_fee = combo.ad_fee
    platform_fee = combo.platform_fee

    # 3. 总成本 + 净利润
    total_cost = material_cost + freight + vat + ad_fee + platform_fee
    profit = combo.sale_price - total_cost

    return {
        "material_cost": round(material_cost, 2),
        "total_cost": round(total_cost, 2),
        "vat": round(vat, 2),
        "profit": round(profit, 2)
    }

# 获取全局财务数据
def get_dashboard_data(db: Session):
    products = db.query(Product).all()
    total_sales = sum([p.sale_price for p in products])
    total_profit = 0
    for p in products:
        if p.type == "组合品":
            profit = calc_combo_profit(db, p.id)["profit"]
        else:
            profit = p.sale_price - (p.cost_price + p.freight + p.sale_price*(p.vat_rate/100) + p.ad_fee + p.platform_fee)
        total_profit += profit
    warn_count = len(db.query(Product).filter(Product.stock <= Product.warn_stock).all())
    return total_sales, round(total_profit, 2), warn_count