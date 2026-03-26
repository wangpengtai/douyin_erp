import requests
import pandas as pd

# 后端接口地址
BASE_URL = "http://127.0.0.1:8000"

# 产品接口
def get_all_products():
    try:
        res = requests.get(f"{BASE_URL}/product/list")
        res.raise_for_status()
        return res.json()
    except Exception as e:
        print(f"获取产品列表失败：{e}")
        return []

def add_product(data):
    try:
        return requests.post(f"{BASE_URL}/product/add", json=data)
    except Exception as e:
        print(f"添加产品失败：{e}")
        return None

def delete_product(pid):
    try:
        return requests.delete(f"{BASE_URL}/product/delete/{pid}")
    except Exception as e:
        print(f"删除产品失败：{e}")
        return None

# 库存接口
def update_stock(pid, stock):
    try:
        return requests.put(f"{BASE_URL}/stock/update", params={"id": pid, "stock": stock})
    except Exception as e:
        print(f"更新库存失败：{e}")
        return None

def get_stock_warn():
    try:
        res = requests.get(f"{BASE_URL}/stock/warn")
        res.raise_for_status()
        return res.json()
    except Exception as e:
        print(f"获取库存预警失败：{e}")
        return []

# 财务接口
def calc_profit(pid):
    try:
        res = requests.get(f"{BASE_URL}/finance/calc/{pid}")
        res.raise_for_status()
        return res.json()
    except Exception as e:
        print(f"计算利润失败：{e}")
        return {}

def get_dashboard():
    try:
        res = requests.get(f"{BASE_URL}/finance/dashboard")
        res.raise_for_status()
        return res.json()
    except Exception as e:
        print(f"获取大盘数据失败：{e}")
        return {"total_sales": 0, "total_profit": 0, "warn_count": 0}

# 批量导入
def import_excel(file):
    try:
        df = pd.read_excel(file)
        count = 0
        for _, row in df.iterrows():
            data = {
                "name": str(row[0]),
                "type": str(row[1]),
                "cost_price": float(row[2]),
                "sale_price": float(row[3]),
                "stock": int(row[4]),
                "warn_stock": 5,
                "freight": float(row[5]),
                "vat_rate": float(row[6]),
                "ad_fee": float(row[7]),
                "platform_fee": float(row[8])
            }
            add_product(data)
            count += 1
        return count
    except Exception as e:
        print(f"导入Excel失败：{e}")
        return 0