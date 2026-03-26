from fastapi import FastAPI
from backend.core.db import engine, Base
from backend.api import product, stock, finance

# 创建数据库表
Base.metadata.create_all(bind=engine)

app = FastAPI(title="抖店进销存管理系统-后端", version="1.0")

# 注册路由
app.include_router(product.router)
app.include_router(stock.router)
app.include_router(finance.router)

@app.get("/")
def root():
    return {"msg": "抖店进销存系统后端运行成功！"}