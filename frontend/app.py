import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent))

import streamlit as st

# ========== 第一步：先设置页面配置（必须是第一个Streamlit命令） ==========
st.set_page_config(
    page_title="抖店进销存系统",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ========== 第二步：多语言配置 ==========
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

# ========== 第三步：优化UI样式（增强所有元素对比度） ==========
st.markdown("""
<style>
    /* 全局背景与字体（核心：强制所有文本为深灰色） */
    html, body, .main {
        background-color: #f0f2f6 !important;
        color: #1f2937 !important;
        font-weight: 500 !important;
    }

    /* 侧边栏样式强化 */
    [data-testid="stSidebar"] {
        background-color: #1f2937 !important;
    }
    [data-testid="stSidebar"] * {
        color: #ffffff !important;
        font-weight: 500 !important;
    }

    /* 按钮样式（增强对比度） */
    .stButton>button {
        border-radius: 10px; 
        height: 45px; 
        font-size: 16px;
        background-color: #2563eb !important;
        color: white !important;
        font-weight: 600 !important;
    }
    .stButton>button:hover {
        background-color: #1d4ed8 !important;
    }

    /* 输入框样式 */
    .stTextInput>div>div, .stNumberInput>div>div, .stSelectbox>div>div {
        border-radius: 8px;
        background-color: white !important;
        color: #1f2937 !important;
    }

    /* 数据卡片样式（强制深文字） */
    div[data-testid="stMetric"] {
        background-color: white !important;
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    }
    div[data-testid="stMetric"] h3, 
    div[data-testid="stMetric"] p {
        color: #1f2937 !important;
        font-weight: 600 !important;
        font-size: 24px !important;
    }

    /* 表格样式（核心修复：表格文字清晰） */
    table, th, td {
        color: #1f2937 !important;
        background-color: white !important;
        font-weight: 500 !important;
        border: 1px solid #e5e7eb !important;
        padding: 8px !important;
    }
    th {
        background-color: #f9fafb !important;
        color: #1f2937 !important;
        font-weight: 700 !important;
    }

    /* 图表样式（强制图表文字为深色） */
    .plotly-container, .plotly * {
        color: #1f2937 !important;
        font-weight: 500 !important;
    }
    svg * {
        fill: #1f2937 !important;
        stroke: #1f2937 !important;
    }

    /* 通用文本样式（覆盖所有遗漏的文本） */
    h1, h2, h3, h4, h5, h6, p, div, span, label {
        color: #1f2937 !important;
        font-weight: 500 !important;
    }

    /* 成功提示框样式 */
    .stSuccess {
        background-color: #dcfce7 !important;
        color: #166534 !important;
        font-weight: 500 !important;
    }
</style>
""", unsafe_allow_html=True)

# ========== 第四步：侧边栏语言选择器（后置，不影响set_page_config） ==========
st.sidebar.selectbox(
    "Language / 语言",
    options=["中文", "English"],
    key="lang",
    index=0
)
# 获取当前语言配置
lang = LANGS[st.session_state.lang]

# ========== 第五步：侧边栏导航（使用多语言） ==========
st.sidebar.title(lang["title"])
st.sidebar.markdown("---")
menu = st.sidebar.radio(
    "功能菜单 / Function Menu",
    [lang["menu_dashboard"], lang["menu_product"], lang["menu_stock"], lang["menu_finance"], lang["menu_import"]]
)

# ========== 第六步：页面路由 ==========
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