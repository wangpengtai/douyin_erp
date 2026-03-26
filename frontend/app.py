import sys
from pathlib import Path
# 一行代码修复路径，确保Python能找到frontend下的所有模块
sys.path.append(str(Path(__file__).resolve().parent))

import streamlit as st

# 苹果风全局配置
st.set_page_config(
    page_title="抖店进销存管理系统",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 全局样式（苹果极简风）
st.markdown("""
<style>
    .main {background-color: #f8f9fa;}
    .stButton>button {border-radius: 10px; height: 45px; font-size: 16px;}
    .stTextInput>div>div {border-radius: 8px;}
    .stNumberInput>div>div {border-radius: 8px;}
    div[data-testid="stMetric"] {
        background-color: white;
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    }
</style>
""", unsafe_allow_html=True)

# 侧边栏导航
st.sidebar.title("🎯 抖店进销存系统")
st.sidebar.markdown("---")
menu = st.sidebar.radio(
    "功能菜单",
    ["📊 数据大盘", "📦 产品管理", "📈 库存管理", "💰 财务税务", "📥 批量导入"]
)

# 页面路由
if menu == "📊 数据大盘":
    from pages.dashboard import show_dashboard
    show_dashboard()
elif menu == "📦 产品管理":
    from pages.product import show_product
    show_product()
elif menu == "📈 库存管理":
    from pages.stock import show_stock
    show_stock()
elif menu == "💰 财务税务":
    from pages.finance import show_finance
    show_finance()
elif menu == "📥 批量导入":
    from pages.import_page import show_import
    show_import()