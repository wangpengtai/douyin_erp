import streamlit as st
from utils.tools import add_product, delete_product, get_all_products

# 新增多语言词典（可抽离到utils统一管理，这里先内置）
PRODUCT_LANG = {
    "中文": {
        "title": "产品 & 组合管理",
        "tab1": "➕ 新增产品",
        "tab2": "🗑️ 删除产品",
        "tab3": "🔗 组合产品绑定",
        "name": "产品名称",
        "type": "产品类型",
        "cost": "原料成本",
        "sale": "销售价格",
        "stock": "库存数量",
        "warn_stock": "库存预警线",
        "freight": "运费/运输费",
        "vat": "增值税率 %",
        "ad_fee": "投流费用",
        "platform_fee": "平台服务费",
        "add_btn": "✅ 添加产品",
        "add_success": "产品添加成功！",
        "delete_title": "删除商品",
        "no_product": "暂无产品",
        "delete_btn": "🗑️ 删除产品",
        "delete_success": "删除成功！",
        "combo_title": "组合品绑定原料（核心功能）",
        "combo_id": "组合品ID",
        "item_id": "原料单品ID",
        "item_num": "原料数量",
        "bind_btn": "🔗 绑定组合",
        "bind_success": "组合绑定成功！"
    },
    "English": {
        "title": "Product & Combo Management",
        "tab1": "➕ Add Product",
        "tab2": "🗑️ Delete Product",
        "tab3": "🔗 Bind Combo Product",
        "name": "Product Name",
        "type": "Product Type",
        "cost": "Material Cost",
        "sale": "Selling Price",
        "stock": "Stock Quantity",
        "warn_stock": "Stock Warning Line",
        "freight": "Freight/Transport Fee",
        "vat": "VAT Rate %",
        "ad_fee": "Ad Fee",
        "platform_fee": "Platform Service Fee",
        "add_btn": "✅ Add Product",
        "add_success": "Product added successfully!",
        "delete_title": "Delete Product",
        "no_product": "No products available",
        "delete_btn": "🗑️ Delete Product",
        "delete_success": "Deleted successfully!",
        "combo_title": "Bind Raw Materials to Combo (Core Function)",
        "combo_id": "Combo Product ID",
        "item_id": "Raw Material ID",
        "item_num": "Raw Material Quantity",
        "bind_btn": "🔗 Bind Combo",
        "bind_success": "Combo bound successfully!"
    }
}

def show_product(lang):
    # 适配当前语言
    pl = PRODUCT_LANG[lang["title"].split(" ")[0] if " " in lang["title"] else "中文"]
    st.title(pl["title"])
    tab1, tab2, tab3 = st.tabs([pl["tab1"], pl["tab2"], pl["tab3"]])

    # 1. 新增产品
    with tab1:
        st.subheader(pl["tab1"])
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input(pl["name"])
            type = st.selectbox(pl["type"], ["单品", "组合品"] if lang["title"] == "抖店进销存系统" else ["Single Product", "Combo Product"])
            cost_price = st.number_input(pl["cost"], 0.0)
            sale_price = st.number_input(pl["sale"], 0.0)
            stock = st.number_input(pl["stock"], 0)
        with col2:
            warn_stock = st.number_input(pl["warn_stock"], 5)
            freight = st.number_input(pl["freight"], 0.0)
            vat_rate = st.number_input(pl["vat"], 13.0)
            ad_fee = st.number_input(pl["ad_fee"], 0.0)
            platform_fee = st.number_input(pl["platform_fee"], 0.0)

        if st.button(pl["add_btn"], type="primary"):
            data = {
                "name": name, "type": type, "cost_price": cost_price,
                "sale_price": sale_price, "stock": stock, "warn_stock": warn_stock,
                "freight": freight, "vat_rate": vat_rate, "ad_fee": ad_fee, "platform_fee": platform_fee
            }
            res = add_product(data)
            st.success(pl["add_success"])

    # 2. 删除产品（其余逻辑保持不变，仅替换文本为pl["xxx"]）
    with tab2:
        st.subheader(pl["delete_title"])
        products = get_all_products()
        if products:
            pid = st.selectbox(
                pl["delete_title"],
                options=[p['id'] for p in products],
                format_func=lambda x: next(p['name'] for p in products if p['id']==x)
            )
            if st.button(pl["delete_btn"]):
                delete_product(pid)
                st.success(pl["delete_success"])
        else:
            st.info(pl["no_product"])

    # 3. 组合产品绑定
    with tab3:
        st.subheader(pl["combo_title"])
        combo_id = st.number_input(pl["combo_id"], 1)
        item_id = st.number_input(pl["item_id"], 1)
        item_num = st.number_input(pl["item_num"], 1)
        if st.button(pl["bind_btn"]):
            st.success(pl["bind_success"])