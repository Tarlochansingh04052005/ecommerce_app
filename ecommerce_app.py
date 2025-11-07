# ecommerce_app.py
import streamlit as st
import pandas as pd
from datetime import datetime
from database_connection import get_connection  # must return mysql.connector connection

st.set_page_config(page_title="ShopSmart — E-Commerce Dashboard", layout="wide", page_icon="🛍️")

# ----------------------------
# Helper functions
# ----------------------------
def fetch_df(query, params=None):
    """Return pandas DataFrame for a read query. Handles connection open/close."""
    conn = get_connection()
    if conn is None:
        return None
    try:
        df = pd.read_sql(query, conn, params=params)
        return df
    except Exception as e:
        st.error(f"Error fetching data: {e}")
        return None
    finally:
        try:
            conn.close()
        except:
            pass

def execute_query(query, params=None):
    """Execute write query (INSERT/UPDATE/DELETE) and commit. Returns success boolean and message."""
    conn = get_connection()
    if conn is None:
        return False, "DB connection failed"
    try:
        cur = conn.cursor()
        if params:
            cur.execute(query, params)
        else:
            cur.execute(query)
        conn.commit()
        return True, "Success"
    except Exception as e:
        return False, str(e)
    finally:
        try:
            cur.close()
            conn.close()
        except:
            pass

def show_sql_error(e):
    st.error(f"SQL Error: {e}")

# ----------------------------
# UI: header + navigation
# ----------------------------
st.markdown("""
<style>

/* === MAIN BACKGROUND === */
.stApp {
    background: linear-gradient(135deg, #1E1F4B 0%, #2B4C7E 40%, #4CA1A3 100%);
    font-family: 'Poppins', sans-serif;
    color: #f5f5f5;
}

/* === SIDEBAR === */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #141E30 0%, #243B55 100%);
    color: #ffffff;
    border-right: 2px solid rgba(255,255,255,0.2);
    box-shadow: 2px 0 10px rgba(0,0,0,0.4);
}
section[data-testid="stSidebar"] h2, section[data-testid="stSidebar"] h3 {
    color: #f9f9f9;
    text-shadow: 0px 1px 3px rgba(0,0,0,0.5);
}
[data-testid="stSidebar"] div[role="radiogroup"] > label {
    background: rgba(255,255,255,0.05);
    border-radius: 10px;
    margin: 5px 0;
    padding: 8px 12px;
    transition: all 0.3s ease;
    font-weight: 600;
    color: #f0f0f0;
}
[data-testid="stSidebar"] div[role="radiogroup"] > label:hover {
    background: rgba(255,255,255,0.2);
    transform: scale(1.03);
    color: #fff;
}

/* === HEADINGS === */
h1, h2, h3 {
    color: #ffffff;
    font-weight: 700;
    text-shadow: 0 2px 5px rgba(0,0,0,0.4);
}

/* === TABLES (DATAFRAMES) === */
.stDataFrame {
    background: rgba(15, 20, 40, 0.8) !important;
    border-radius: 12px !important;
    box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    padding: 10px;
}

table {
    color: #e6e6e6 !important;
    border-collapse: collapse;
    background: rgba(30, 35, 60, 0.85);
}
th {
    background: linear-gradient(90deg, #00C6FF, #0072FF);
    color: #ffffff !important;
    font-weight: 700;
    padding: 10px;
}
td {
    background: rgba(255,255,255,0.05);
    padding: 10px;
}
tr:nth-child(even) {
    background: rgba(255,255,255,0.08);
}
tr:hover {
    background: rgba(0,114,255,0.2);
    transition: 0.3s;
}

/* === BUTTONS === */
div.stButton > button {
    background: linear-gradient(90deg, #00C6FF 0%, #0072FF 100%);
    color: white;
    font-weight: 600;
    border-radius: 10px;
    border: none;
    padding: 0.6rem 1.4rem;
    box-shadow: 0 3px 10px rgba(0,0,0,0.4);
    transition: all 0.3s ease-in-out;
}
div.stButton > button:hover {
    background: linear-gradient(90deg, #6A11CB 0%, #2575FC 100%);
    transform: scale(1.07);
}

/* === METRICS === */
div[data-testid="metric-container"] {
    background: rgba(255,255,255,0.1);
    border-radius: 12px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.3);
    color: #fff;
}

/* === INPUTS === */
.stSelectbox, .stTextInput, .stNumberInput {
    background-color: rgba(255,255,255,0.1) !important;
    border: 1px solid rgba(255,255,255,0.2) !important;
    color: white !important;
    border-radius: 8px !important;
}
.stSelectbox div, .stTextInput input, .stNumberInput input {
    color: #fff !important;
}

/* === SCROLLBAR === */
::-webkit-scrollbar {
    width: 10px;
}
::-webkit-scrollbar-thumb {
    background: linear-gradient(180deg, #00C6FF 0%, #0072FF 100%);
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

st.markdown("<div class='big-title'>🛍️ ShopSmart — E-Commerce & Order Management</div>", unsafe_allow_html=True)
st.markdown("A demo project for your B.Com (Hons) Business Analytics portfolio — Streamlit + MySQL")

# Sidebar menu
with st.sidebar:
    st.markdown("## 🔎 Navigation")
    page = st.radio("", ["Dashboard", "Customers", "Products", "Orders", "Inventory", "Analytics", "Export/Settings"])

# ----------------------------
# DASHBOARD
# ----------------------------
if page == "Dashboard":
    st.header("Dashboard Overview")
    col1, col2, col3, col4 = st.columns(4)

    # metrics
    customers_df = fetch_df("SELECT COUNT(*) AS cnt FROM Customers")
    products_df = fetch_df("SELECT COUNT(*) AS cnt FROM Products")
    orders_df = fetch_df("SELECT COUNT(*) AS cnt FROM Orders")
    revenue_df = fetch_df("SELECT IFNULL(SUM(total_amount),0) AS revenue FROM Orders")

    customers = int(customers_df['cnt'][0]) if customers_df is not None else 0
    products = int(products_df['cnt'][0]) if products_df is not None else 0
    orders = int(orders_df['cnt'][0]) if orders_df is not None else 0
    revenue = float(revenue_df['revenue'][0]) if revenue_df is not None else 0.0

    col1.metric("Customers", customers)
    col2.metric("Products", products)
    col3.metric("Orders", orders)
    col4.metric("Total Revenue (₹)", f"{revenue:,.2f}")

    st.markdown("---")
    left, right = st.columns((2,1))

    with left:
        st.subheader("Recent Orders")
        recent = fetch_df("SELECT o.order_id, o.customer_id, c.first_name, o.order_date, o.total_amount, o.status "
                          "FROM Orders o LEFT JOIN Customers c ON o.customer_id = c.customer_id "
                          "ORDER BY o.order_date DESC LIMIT 10")
        if recent is not None:
            st.dataframe(recent)
        else:
            st.info("No recent orders (or DB connection failed).")

    with right:
        st.subheader("Low Stock Products")
        low = fetch_df("SELECT product_id, product_name, stock_quantity FROM Products WHERE stock_quantity <= 10 ORDER BY stock_quantity ASC")
        if low is not None and not low.empty:
            st.table(low)
        else:
            st.write("No products low in stock (<=10).")

# ----------------------------
# CUSTOMERS (CRUD)
# ----------------------------
elif page == "Customers":
    st.header("Customers — View / Add / Edit / Delete")
    tab1, tab2 = st.tabs(["View Customers", "Add / Edit Customer"])

    with tab1:
        df = fetch_df("SELECT * FROM Customers")
        if df is not None:
            st.dataframe(df)
        else:
            st.error("Unable to load customers — check DB connection.")

    with tab2:
        st.subheader("Add a new customer")
        with st.form("add_customer", clear_on_submit=True):
            fname = st.text_input("First name")
            lname = st.text_input("Last name")
            email = st.text_input("Email")
            phone = st.text_input("Mobile number")
            reg_date = st.date_input("Registered date", value=datetime.today())
            submitted = st.form_submit_button("Add Customer")
            if submitted:
                if not fname or not email:
                    st.error("Please provide name and email.")
                else:
                    q = "INSERT INTO Customers (customer_id, first_name, last_name, email, mobile_number, registered_date) VALUES (%s,%s,%s,%s,%s,%s)"
                    # generate customer_id as MAX+1 if not auto-increment in your schema
                    # fetch max id
                    maxid_df = fetch_df("SELECT IFNULL(MAX(customer_id),0) AS mx FROM Customers")
                    new_id = int(maxid_df['mx'][0]) + 1 if maxid_df is not None else 1
                    success, msg = execute_query(q, (new_id, fname, lname, email, phone, reg_date.strftime("%Y-%m-%d")))
                    if success:
                        st.success("Customer added successfully.")
                    else:
                        show_sql_error(msg)

        st.markdown("---")
        st.subheader("Edit / Delete Customer")
        df2 = fetch_df("SELECT customer_id, first_name, last_name, email FROM Customers")
        if df2 is not None and not df2.empty:
            selected = st.selectbox("Select customer", df2.apply(lambda r: f'{r.customer_id} - {r.first_name} {r.last_name} ({r.email})', axis=1))
            selected_id = int(selected.split(" - ")[0])
            c_record = fetch_df("SELECT * FROM Customers WHERE customer_id = %s", params=(selected_id,))
            if c_record is not None and not c_record.empty:
                rec = c_record.iloc[0]
                col1, col2 = st.columns(2)
                with col1:
                    new_fname = st.text_input("First name", value=rec.first_name)
                    new_lname = st.text_input("Last name", value=rec.last_name)
                with col2:
                    new_email = st.text_input("Email", value=rec.email)
                    new_phone = st.text_input("Mobile", value=rec.mobile_number)
                if st.button("Update Customer"):
                    q_up = "UPDATE Customers SET first_name=%s, last_name=%s, email=%s, mobile_number=%s WHERE customer_id=%s"
                    ok, m = execute_query(q_up, (new_fname, new_lname, new_email, new_phone, selected_id))
                    if ok:
                        st.success("Customer updated.")
                    else:
                        show_sql_error(m)
                if st.button("Delete Customer"):
                    # caution: this will fail if FK constraints exist; handle or cascade as per schema
                    ok, m = execute_query("DELETE FROM Customers WHERE customer_id=%s", (selected_id,))
                    if ok:
                        st.success("Customer deleted.")
                    else:
                        show_sql_error(m)
        else:
            st.info("No customers found to edit/delete.")

# ----------------------------
# PRODUCTS (CRUD + quick stock adjust)
# ----------------------------
elif page == "Products":
    st.header("Products — Inventory & Management")
    tab1, tab2 = st.tabs(["View Products", "Add / Edit Product"])

    with tab1:
        df = fetch_df("SELECT p.product_id, p.product_name, c.category_name, p.price, p.stock_quantity, s.supplier_name "
                      "FROM Products p LEFT JOIN Categories c ON p.category_id = c.category_id "
                      "LEFT JOIN Suppliers s ON p.supplier_id = s.supplier_id")
        if df is not None:
            st.dataframe(df)
        else:
            st.error("Unable to load products.")

    with tab2:
        st.subheader("Add a new product")
        cats = fetch_df("SELECT category_id, category_name FROM Categories")
        sups = fetch_df("SELECT supplier_id, supplier_name FROM Suppliers")
        with st.form("add_product", clear_on_submit=True):
            name = st.text_input("Product name")
            cat = st.selectbox("Category", options=cats['category_name'] if cats is not None else [])
            sup = st.selectbox("Supplier", options=sups['supplier_name'] if sups is not None else [])
            price = st.number_input("Price (₹)", min_value=0.0, value=100.0, step=1.0)
            stock = st.number_input("Stock qty", min_value=0, value=10)
            submitted = st.form_submit_button("Add Product")
            if submitted:
                # map names back to ids
                cat_id = int(cats.loc[cats['category_name'] == cat, 'category_id'].values[0]) if cats is not None else None
                sup_id = int(sups.loc[sups['supplier_name'] == sup, 'supplier_id'].values[0]) if sups is not None else None
                maxid_df = fetch_df("SELECT IFNULL(MAX(product_id),0) AS mx FROM Products")
                new_id = int(maxid_df['mx'][0]) + 1 if maxid_df is not None else 1
                q = "INSERT INTO Products (product_id, category_id, supplier_id, product_name, price, stock_quantity) VALUES (%s,%s,%s,%s,%s,%s)"
                ok, m = execute_query(q, (new_id, cat_id, sup_id, name, price, stock))
                if ok:
                    st.success("Product added successfully.")
                else:
                    show_sql_error(m)

        st.markdown("---")
        st.subheader("Edit / Adjust Product Stock")
        prod_df = fetch_df("SELECT product_id, product_name FROM Products")
        if prod_df is not None and not prod_df.empty:
            sel = st.selectbox("Select product", prod_df.apply(lambda r: f"{r.product_id} - {r.product_name}", axis=1))
            pid = int(sel.split(" - ")[0])
            prod_rec = fetch_df("SELECT * FROM Products WHERE product_id=%s", params=(pid,))
            if prod_rec is not None and not prod_rec.empty:
                p = prod_rec.iloc[0]
                cols = st.columns(3)
                new_name = cols[0].text_input("Name", value=p.product_name)
                new_price = cols[1].number_input("Price", value=float(p.price))
                adjust = cols[2].number_input("Adjust stock by (±)", value=0, step=1)
                if st.button("Update Product"):
                    ok, m = execute_query("UPDATE Products SET product_name=%s, price=%s WHERE product_id=%s", (new_name, new_price, pid))
                    if ok:
                        st.success("Product updated.")
                    else:
                        show_sql_error(m)
                if st.button("Apply stock adjustment"):
                    ok, m = execute_query("UPDATE Products SET stock_quantity = stock_quantity + %s WHERE product_id=%s", (adjust, pid))
                    if ok:
                        st.success("Stock updated.")
                    else:
                        show_sql_error(m)
        else:
            st.info("No products to edit.")

# ----------------------------
# ORDERS (View, Create simple order)
# ----------------------------
elif page == "Orders":
    st.header("Orders — Create and View Orders")
    tab1, tab2 = st.tabs(["All Orders", "Create Order"])

    with tab1:
        df = fetch_df("SELECT o.order_id, c.first_name, o.order_date, o.total_amount, o.status "
                      "FROM Orders o LEFT JOIN Customers c ON o.customer_id=c.customer_id ORDER BY o.order_date DESC")
        if df is not None:
            st.dataframe(df)
        else:
            st.error("Unable to load orders.")

    with tab2:
        st.subheader("Place a new order (simple flow)")
        customers = fetch_df("SELECT customer_id, first_name FROM Customers")
        products = fetch_df("SELECT product_id, product_name, price, stock_quantity FROM Products")
        if customers is None or products is None:
            st.error("Cannot load customers or products. Check DB connection.")
        else:
            csel = st.selectbox("Customer", options=customers.apply(lambda r: f"{r.customer_id} - {r.first_name}", axis=1))
            cust_id = int(csel.split(" - ")[0])
            psel = st.selectbox("Product", options=products.apply(lambda r: f"{r.product_id} - {r.product_name} (₹{r.price}) [stock:{r.stock_quantity}]", axis=1))
            pid = int(psel.split(" - ")[0])
            qty = st.number_input("Quantity", min_value=1, value=1)
            # fetch price & stock
            pinfo = products[products['product_id'] == pid].iloc[0]
            if qty > int(pinfo.stock_quantity):
                st.warning("Quantity greater than available stock.")
            total_price = float(pinfo.price) * qty
            st.write(f"**Total:** ₹{total_price:,.2f}")

            if st.button("Place Order"):
                # create order_id
                maxid_df = fetch_df("SELECT IFNULL(MAX(order_id),0) AS mx FROM Orders")
                new_oid = int(maxid_df['mx'][0]) + 1 if maxid_df is not None else 1
                q1 = "INSERT INTO Orders (order_id, customer_id, order_date, total_amount, status) VALUES (%s,%s,%s,%s,%s)"
                ok1, msg1 = execute_query(q1, (new_oid, cust_id, datetime.now().strftime("%Y-%m-%d"), total_price, "Pending"))
                if not ok1:
                    show_sql_error(msg1)
                else:
                    # order_detail
                    maxod = fetch_df("SELECT IFNULL(MAX(order_detail_id),0) AS mx FROM Order_Detail")
                    new_od = int(maxod['mx'][0]) + 1 if maxod is not None else 1
                    q2 = "INSERT INTO Order_Detail (order_detail_id, order_id, product_id, quantity, price) VALUES (%s,%s,%s,%s,%s)"
                    ok2, msg2 = execute_query(q2, (new_od, new_oid, pid, qty, float(pinfo.price)))
                    if not ok2:
                        show_sql_error(msg2)
                    else:
                        # reduce inventory
                        ok3, msg3 = execute_query("UPDATE Products SET stock_quantity = stock_quantity - %s WHERE product_id=%s", (qty, pid))
                        if not ok3:
                            show_sql_error(msg3)
                        else:
                            st.success(f"Order {new_oid} placed successfully (status: Pending).")

# ----------------------------
# INVENTORY (view + bulk import)
# ----------------------------
elif page == "Inventory":
    st.header("Inventory — Current Stock")
    df = fetch_df("SELECT product_id, product_name, stock_quantity FROM Products ORDER BY stock_quantity ASC")
    if df is not None:
        st.dataframe(df)
    else:
        st.error("Cannot load inventory.")

    st.markdown("---")
    st.subheader("Bulk stock update (CSV)")
    st.markdown("Upload CSV with columns: product_id, stock_quantity (absolute value to set)")
    uploaded = st.file_uploader("Upload CSV", type=["csv"])
    if uploaded:
        try:
            updf = pd.read_csv(uploaded)
            if "product_id" in updf.columns and "stock_quantity" in updf.columns:
                for _, row in updf.iterrows():
                    execute_query("UPDATE Products SET stock_quantity=%s WHERE product_id=%s", (int(row.stock_quantity), int(row.product_id)))
                st.success("Bulk stock updated.")
            else:
                st.error("CSV must contain product_id and stock_quantity columns.")
        except Exception as e:
            st.error(f"Error processing file: {e}")

# ----------------------------
# ANALYTICS (charts)
# ----------------------------
elif page == "Analytics":
    st.header("Sales & Inventory Analytics")
    st.subheader("Revenue by Month")
    rev = fetch_df("SELECT DATE_FORMAT(order_date, '%Y-%m') AS month, SUM(total_amount) AS revenue FROM Orders GROUP BY month ORDER BY month")
    if rev is not None and not rev.empty:
        rev['month'] = pd.to_datetime(rev['month'])
        rev = rev.sort_values('month')
        st.line_chart(data=rev.set_index('month')['revenue'])
    else:
        st.info("Not enough order data for revenue chart.")

    st.subheader("Top Products by Sales (count)")
    top = fetch_df("SELECT p.product_name, SUM(od.quantity) AS qty_sold FROM Order_Detail od JOIN Products p ON od.product_id=p.product_id GROUP BY od.product_id ORDER BY qty_sold DESC LIMIT 10")
    if top is not None and not top.empty:
        st.bar_chart(data=top.set_index('product_name')['qty_sold'])
    else:
        st.info("No order_detail data to show top products.")

    st.subheader("Category-wise Revenue")
    catrev = fetch_df("SELECT c.category_name, SUM(od.quantity * od.price) AS revenue FROM Order_Detail od JOIN Products p ON od.product_id=p.product_id JOIN Categories c ON p.category_id=c.category_id GROUP BY c.category_id ORDER BY revenue DESC")
    if catrev is not None and not catrev.empty:
        st.dataframe(catrev)
    else:
        st.info("No category revenue data available.")

# ----------------------------
# EXPORT / SETTINGS
# ----------------------------
elif page == "Export/Settings":
    st.header("Export & Settings")
    st.subheader("Export Tables to CSV")
    table = st.selectbox("Select table to export", ["Customers","Products","Orders","Order_Detail","Payments","Reviews","Wishlist","Cart"])
    if st.button("Export CSV"):
        dfx = fetch_df(f"SELECT * FROM {table}")
        if dfx is not None:
            csv = dfx.to_csv(index=False).encode('utf-8')
            st.download_button(label=f"Download {table}.csv", data=csv, file_name=f"{table}.csv", mime='text/csv')
        else:
            st.error("Failed to fetch table (DB issue).")

    st.markdown("---")
    st.subheader("DB Connection Test")
    if st.button("Test Connection"):
        conn = get_connection()
        if conn is None:
            st.error("❌ DB connection failed. Check credentials and DB status.")
        else:
            try:
                cur = conn.cursor()
                cur.execute("SELECT 1")
                st.success("✅ DB connection working.")
            except Exception as e:
                st.error(f"❌ DB test failed: {e}")
            finally:
                try:
                    cur.close()
                    conn.close()
                except:
                    pass

st.markdown("<br><br><center>Made with TARUN — ShopSmart demo app for university project</center>", unsafe_allow_html=True)
