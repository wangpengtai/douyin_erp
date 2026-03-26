import streamlit as st
from utils.tools import get_all_products

def show_dashboard(lang):
    """显示数据大盘页面"""
    # 页面标题
    st.title(lang["title"])
    st.subheader(lang["dashboard_subtitle"])
    
    # 模拟数据（实际项目中应从数据库获取）
    total_sales = 125000.0
    total_profit = 32000.0
    total_products = len(get_all_products())
    low_stock_count = 2
    
    # 数据卡片
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(lang["dashboard_sales"], f"¥{total_sales:,.2f}")
    with col2:
        st.metric(lang["dashboard_profit"], f"¥{total_profit:,.2f}")
    with col3:
        st.metric(lang["dashboard_products"], total_products)
    with col4:
        st.metric(lang["dashboard_warn"], low_stock_count)
    
    # 低库存预警
    st.markdown("---")
    st.subheader(lang["dashboard_warn_title"])
    
    # 模拟低库存商品数据
    low_stock_products = [
        {"id": 1, "name": "产品A", "stock": 3, "warn_stock": 5},
        {"id": 2, "name": "产品B", "stock": 2, "warn_stock": 10}
    ]
    
    if low_stock_products:
        st.table(low_stock_products)
    else:
        st.success(lang["dashboard_warn_ok"])
    
    # 产品库存统计图表
    st.markdown("---")
    st.subheader(lang["dashboard_chart_title"])
    
    # 模拟库存数据
    products = get_all_products()
    if products:
        product_names = [p["name"] for p in products]
        stock_values = [p["stock"] for p in products]
        
        # 使用Streamlit的内置图表
        st.bar_chart({
            "库存数量": stock_values
        }, use_container_width=True)
    else:
        st.info("暂无产品数据")