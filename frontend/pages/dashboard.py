import streamlit as st
import plotly.express as px
from utils.tools import get_dashboard, get_stock_warn, get_all_products

# 接收语言参数
def show_dashboard(lang):
    st.title(lang["menu_dashboard"])
    st.markdown(f"<p style='color:#4b5563; font-size:16px; font-weight:500'>{lang['dashboard_subtitle']}</p>", unsafe_allow_html=True)
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

    # 库存预警列表（强制表格样式）
    st.subheader(lang["dashboard_warn_title"])
    if warn_list:
        # 转换为更易读的格式，避免原始字段名混乱
        clean_warn_list = []
        for item in warn_list:
            clean_warn_list.append({
                "产品ID": item.get("id", ""),
                "产品名称": item.get("name", ""),
                "产品类型": item.get("type", ""),
                "当前库存": item.get("stock", 0),
                "预警库存": item.get("warn_stock", 5),
                "成本价": f"¥{item.get('cost_price', 0)}",
                "售价": f"¥{item.get('sale_price', 0)}"
            })
        st.table(clean_warn_list)  # 展示清洗后的表格
    else:
        st.success(lang["dashboard_warn_ok"])

    # 库存可视化图表（强化文字颜色）
    if products:
        st.subheader(lang["dashboard_chart_title"])
        names = [p['name'] for p in products]
        stocks = [p['stock'] for p in products]
        fig = px.bar(
            x=names, y=stocks,
            title=lang["dashboard_chart_title"],
            template="plotly_white",  # 更清晰的白色模板
            color_discrete_sequence=["#2563eb"]  # 统一品牌色
        )
        # 强制图表所有文字为深灰色
        fig.update_layout(
            font=dict(color="#1f2937", size=14, weight="500"),
            plot_bgcolor="#f0f2f6",
            paper_bgcolor="#f0f2f6",
            title_font=dict(color="#1f2937", size=16, weight="700"),
            xaxis_title_font=dict(color="#1f2937", weight="600"),
            yaxis_title_font=dict(color="#1f2937", weight="600")
        )
        # 坐标轴文字强化
        fig.update_xaxes(tickfont=dict(color="#1f2937", weight="500"))
        fig.update_yaxes(tickfont=dict(color="#1f2937", weight="500"))
        st.plotly_chart(fig, use_container_width=True)