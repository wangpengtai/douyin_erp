import streamlit as st
import plotly.express as px
from utils.tools import get_dashboard, get_stock_warn, get_all_products

def show_dashboard():
    st.title("📊 经营数据大盘")
    st.markdown("<p style='color:#666'>实时经营数据 · 本地安全存储</p>", unsafe_allow_html=True)
    st.markdown("---")

    # 获取核心数据
    data = get_dashboard()
    products = get_all_products()
    warn_list = get_stock_warn()

    # 苹果风数据卡片
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("💰 总销售额", f"¥{data.get('total_sales',0)}")
    with col2:
        st.metric("✅ 总净利润", f"¥{data.get('total_profit',0)}")
    with col3:
        st.metric("📦 产品总数", len(products))
    with col4:
        st.metric("⚠️ 库存预警", len(warn_list))

    st.markdown("---")

    # 库存预警列表
    st.subheader("🚨 低库存预警商品")
    if warn_list:
        st.table(warn_list)
    else:
        st.success("✅ 所有商品库存充足！")

    # 库存可视化图表
    if products:
        st.subheader("📊 产品库存统计")
        names = [p['name'] for p in products]
        stocks = [p['stock'] for p in products]
        fig = px.bar(
            x=names, y=stocks,
            title="产品库存数量",
            template="simple_white",
            color_discrete_sequence=["#0071e3"]
        )
        st.plotly_chart(fig, use_container_width=True)