import streamlit as st
import requests
from utils.tools import update_stock, get_stock_warn

def show_stock():
    st.title("📈 库存管理")
    product_id = st.number_input("产品ID", min_value=1)
    new_stock = st.number_input("新库存数量", min_value=0)
    if st.button("更新库存"):
        requests.put(f"{BASE_URL}/stock/update", params={"id": product_id, "stock": new_stock})
        st.success("库存更新成功！")