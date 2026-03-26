import streamlit as st
import requests
from utils.tools import add_product, delete_product, get_all_products

def show_product():
    st.title("📦 产品 & 组合管理")
    tab1, tab2 = st.tabs(["新增产品", "组合产品绑定"])
    
    with tab1:
        with st.form("新增产品"):
            name = st.text_input("产品名称")
            type = st.selectbox("产品类型", ["单品", "组合品"])
            cost = st.number_input("原料成本", min_value=0.0)
            sale = st.number_input("售价", min_value=0.0)
            stock = st.number_input("库存", min_value=0)
            warn = st.number_input("库存预警线", min_value=0, value=5)
            # 全成本
            freight = st.number_input("运费", min_value=0.0)
            vat = st.number_input("增值税率(%)", min_value=0.0, value=13.0)
            ad = st.number_input("投流费用", min_value=0.0)
            platform = st.number_input("平台服务费", min_value=0.0)
            
            if st.form_submit_button("添加产品"):
                data = {
                    "name": name, "type": type, "cost_price": cost,
                    "sale_price": sale, "stock": stock, "warn_stock": warn,
                    "freight": freight, "vat_rate": vat, "ad_fee": ad, "platform_fee": platform
                }
                res = requests.post(f"{BASE_URL}/product/add", json=data)
                st.success("产品添加成功！")
    
    with tab2:
        st.subheader("绑定组合产品")
        combo_id = st.number_input("组合品ID", min_value=1)
        item_id = st.number_input("子单品ID", min_value=1)
        num = st.number_input("单品数量", min_value=1, value=1)
        if st.button("绑定"):
            requests.post(f"{BASE_URL}/product/bind_combine", params={"combo_id": combo_id, "item_id": item_id, "num": num})
            st.success("组合绑定成功！")