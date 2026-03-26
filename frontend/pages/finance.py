import streamlit as st
import requests
from utils.tools import calc_profit, get_dashboard

def show_finance():
    st.title("💰 财务 & 税务核算")
    combo_id = st.number_input("组合品ID", min_value=1)
    if st.button("计算成本利润"):
        data = requests.get(f"{BASE_URL}/finance/calc/{combo_id}").json()
        st.markdown(f"""
        **原料成本**: ¥{data['material_cost']}  
        **增值税**: ¥{data['vat']}  
        **总成本**: ¥{data['total_cost']}  
        **净利润**: ¥{data['profit']}
        """)