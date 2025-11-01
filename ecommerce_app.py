import streamlit as st
import pandas as pd
from database_connection import get_connection
from datetime import datetime

# --- Page Setup ---
st.set_page_config(page_title="E-Commerce Management", layout="wide", page_icon="🛒")
st.title("🛍️ E-Commerce & Order Management System")

# --- Sidebar Menu ---
menu = st.sidebar.selectbox(
    "📂 Navigation",
    ["Dashboard", "Customers", "Products", "Orders", "Add New Order", "Payments", "Reviews"]
)

# --- Dashboard ---
if menu == "Dashboard":
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM Customers")
    customers = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM Products")
    products = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM Orders")
    orders = cur.fetchone()[0]
    cur.execute("SELECT SUM(total_amount) FROM Orders")
    revenue = cur.fetchone()[0] or 0

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Customers", customers)
    col2.metric("Products", products)
    col3.metric("Orders", orders)
    col4.metric("Total Revenue (₹)", f"{revenue:,.2f}")

    st.subheader("🧾 Recent Orders")
    df = pd.read_sql(
        "SELECT order_id, customer_id, order_date, total_amount, status FROM Orders ORDER BY order_date DESC LIMIT 10",
        conn
    )
    st.dataframe(df)
    conn.close()

# --- Customers ---
elif menu == "Customers":
    conn = get_connection()
    df = pd.read_sql("SELECT * FROM Customers", conn)
    st.subheader("👥 Customer Records")
    st.dataframe(df)
    conn.close()

# --- Products ---
elif menu == "Products":
    conn = get_connection()
    df = pd.read_sql(
        """SELECT p.product_id, p.product_name, c.category_name, p.price, p.stock_quantity
           FROM Products p JOIN Categories c ON p.category_id = c.category_id""",
        conn
    )
    st.subheader("📦 Product Inventory")
    st.dataframe(df)
    conn.close()

# --- Orders ---
elif menu == "Orders":
    conn = get_connection()
    df = pd.read_sql(
        """SELECT o.order_id, c.first_name, o.order_date, o.total_amount, o.status
           FROM Orders o JOIN Customers c ON o.customer_id = c.customer_id
           ORDER BY o.order_date DESC""",
        conn
    )
    st.subheader("🧾 All Orders")
    st.dataframe(df)
    conn.close()

# --- Add New Order ---
elif menu == "Add New Order":
    conn = get_connection()
    cur = conn.cursor()

    st.subheader("➕ Create New Order")
    customers_df = pd.read_sql("SELECT customer_id, first_name FROM Customers", conn)
    products_df = pd.read_sql("SELECT product_id, product_name, price FROM Products", conn)

    customer = st.selectbox("Select Customer", customers_df["first_name"])
    customer_id = int(customers_df.loc[customers_df["first_name"] == customer, "customer_id"].values[0])

    product = st.selectbox("Select Product", products_df["product_name"])
    product_data = products_df[products_df["product_name"] == product].iloc[0]
    quantity = st.number_input("Quantity", min_value=1, value=1)
    total = product_data["price"] * quantity
    st.write(f"💰 Total Amount: ₹{total}")

    if st.button("Place Order"):
        cur.execute(
            "INSERT INTO Orders (customer_id, order_date, total_amount, status) VALUES (%s,%s,%s,%s)",
            (customer_id, datetime.now().strftime("%Y-%m-%d"), total, "Pending")
        )
        conn.commit()
        st.success("✅ Order added successfully!")
    conn.close()

# --- Payments ---
elif menu == "Payments":
    conn = get_connection()
    df = pd.read_sql("SELECT * FROM Payments", conn)
    st.subheader("💳 Payments")
    st.dataframe(df)
    conn.close()

# --- Reviews ---
elif menu == "Reviews":
    conn = get_connection()
    df = pd.read_sql(
        """SELECT r.review_id, p.product_name, c.first_name, r.rating, r.review_text
           FROM Reviews r
           JOIN Products p ON r.product_id = p.product_id
           JOIN Customers c ON r.customer_id = c.customer_id""",
        conn
    )
    st.subheader("⭐ Customer Reviews")
    st.dataframe(df)
    conn.close()