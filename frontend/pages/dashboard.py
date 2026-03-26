import streamlit as st
import plotly.express as px
from utils.tools import get_dashboard, get_stock_warn, get_all_products

# 接收语言参数
def show_dashboard(lang):
    st.title(lang["menu_dashboard"])
    st.markdown(f"<p style='color:#4b5563; font-size:16px'>{lang['dashboard_subtitle']}</p>", unsafe_allow_html=True)
    st.markdown("---")

    # 获取核心数据
    data = get_dashboard()
    products = get_all_products()
    warn_list = get_stock_warn()

    # 数据卡片（增强对比度）
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(f"💰 {lang['dashboard_sales']}", f"¥{data.get('total_sales',0)}")
    with col2:
        st.metric(f"✅ {lang['dashboard_profit']}", f"¥{data.get('total_profit',0)}")
    with col3:
        st.metric(f"📦 {lang['dashboard_products']}", len(products))
    with col4:
        st.metric(f"⚠️ {lang['dashboard_warn']}", len(warn_list))

    st.markdown("---")

    # 库存预警列表
    st.subheader(lang["dashboard_warn_title"])
    if warn_list:
        st.table(warn_list)
    else:
        st.success(lang["dashboard_warn_ok"])

    # 库存可视化图表
    if products:
        st.subheader(lang["dashboard_chart_title"])
        names = [p['name'] for p in products]
        stocks = [p['stock'] for p in products]
        fig = px.bar(
            x=names, y=stocks,
            title=lang["dashboard_chart_title"],
            template="simple_white",
            color_discrete_sequence=["#2563eb"]  # 统一品牌色
        )
        # 优化图表文字对比度
        fig.update_layout(
            font=dict(color="#1f2937"),
            plot_bgcolor="#f0f2f6",
            paper_bgcolor="#f0f2f6"
        )
        st.plotly_chart(fig, use_container_width=True)