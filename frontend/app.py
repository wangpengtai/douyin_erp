import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent))

import streamlit as st

# ========== 新增：多语言配置 ==========
# 定义中英双语词典
LANGS = {
    "中文": {
        "title": "抖店进销存系统",
        "menu_dashboard": "📊 数据大盘",
        "menu_product": "📦 产品管理",
        "menu_stock": "📈 库存管理",
        "menu_finance": "💰 财务税务",
        "menu_import": "📥 批量导入",
        "dashboard_subtitle": "实时经营数据 · 本地安全存储",
        "dashboard_sales": "总销售额",
        "dashboard_profit": "总净利润",
        "dashboard_products": "产品总数",
        "dashboard_warn": "库存预警",
        "dashboard_warn_title": "🚨 低库存预警商品",
        "dashboard_warn_ok": "✅ 所有商品库存充足！",
        "dashboard_chart_title": "产品库存统计"
    },
    "English": {
        "title": "Douyin Shop Inventory System",
        "menu_dashboard": "📊 Dashboard",
        "menu_product": "📦 Product Management",
        "menu_stock": "📈 Stock Management",
        "menu_finance": "💰 Finance & Tax",
        "menu_import": "📥 Batch Import",
        "dashboard_subtitle": "Real-time Business Data · Local Secure Storage",
        "dashboard_sales": "Total Sales",
        "dashboard_profit": "Total Net Profit",
        "dashboard_products": "Total Products",
        "dashboard_warn": "Stock Warnings",
        "dashboard_warn_title": "🚨 Low Stock Warning Products",
        "dashboard_warn_ok": "✅ All products have sufficient stock!",
        "dashboard_chart_title": "Product Stock Statistics"
    }
}

# 侧边栏语言选择器
st.sidebar.selectbox(
    "Language / 语言",
    options=["中文", "English"],
    key="lang",
    index=0
)
# 获取当前语言配置
lang = LANGS[st.session_state.lang]

# ========== 优化：UI样式（增强对比度） ==========
st.set_page_config(
    page_title=lang["title"],
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 自定义CSS（核心优化：增强字体/背景对比度，苹果风更清晰）
st.markdown("""
<style>
    /* 全局背景与字体 */
    .main {background-color: #f0f2f6; color: #1f2937;}
    /* 侧边栏样式 */
    [data-testid="stSidebar"] {background-color: #1f2937;}
    [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] p, [data-testid="stSidebar"] label {color: #ffffff !important;}
    /* 按钮样式（增强对比度） */
    .stButton>button {
        border-radius: 10px; 
        height: 45px; 
        font-size: 16px;
        background-color: #2563eb;
        color: white !important;
    }
    .stButton>button:hover {background-color: #1d4ed8;}
    /* 输入框样式 */
    .stTextInput>div>div, .stNumberInput>div>div, .stSelectbox>div>div {
        border-radius: 8px;
        background-color: white;
        color: #1f2937;
    }
    /* 数据卡片样式（增强对比度） */
    div[data-testid="stMetric"] {
        background-color: white;
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        color: #1f2937 !important;
    }
    div[data-testid="stMetric"] h3 {color: #4b5563 !important;}
    div[data-testid="stMetric"] p {color: #1f2937 !important; font-size: 24px !important; font-weight: 600;}
    /* 文本样式 */
    h1, h2, h3, h4, p, div {color: #1f2937 !important;}
    .stSuccess {background-color: #dcfce7; color: #166534 !important;}
</style>
""", unsafe_allow_html=True)

# ========== 侧边栏导航（使用多语言） ==========
st.sidebar.title(lang["title"])
st.sidebar.markdown("---")
menu = st.sidebar.radio(
    "功能菜单 / Function Menu",
    [lang["menu_dashboard"], lang["menu_product"], lang["menu_stock"], lang["menu_finance"], lang["menu_import"]]
)

# ========== 页面路由 ==========
if menu == lang["menu_dashboard"]:
    from pages.dashboard import show_dashboard
    show_dashboard(lang)  # 传递语言配置
elif menu == lang["menu_product"]:
    from pages.product import show_product
    show_product(lang)
elif menu == lang["menu_stock"]:
    from pages.stock import show_stock
    show_stock(lang)
elif menu == lang["menu_finance"]:
    from pages.finance import show_finance
    show_finance(lang)
elif menu == lang["menu_import"]:
    from pages.import_page import show_import
    show_import(lang)