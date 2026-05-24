import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# --- Load Dataset ---
data = pd.read_csv("sales.csv")

# --- Sidebar Navigation ---
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Sales", "Trends", "Summary"])

# --- KPI Section (Reusable) ---
def show_kpis(df):
    total_sales = df["Sales"].sum()
    avg_sales = df["Sales"].mean()
    num_records = len(df)

    st.metric("Total Sales", f"{total_sales:,.0f}")
    st.metric("Average Sales", f"{avg_sales:,.2f}")
    st.metric("Records", num_records)

# --- Page 1: Sales ---
if page == "Sales":
    st.title("📊 Sales Dashboard")
    st.write("### Filtered Data Table")
    st.dataframe(data)

    st.write("### KPIs")
    show_kpis(data)

    st.write("### Sales by Product")
    sales_by_product = data.groupby("Product")["Sales"].sum()
    fig, ax = plt.subplots()
    sns.barplot(x=sales_by_product.index, y=sales_by_product.values, ax=ax, palette="viridis")
    st.pyplot(fig)

# --- Page 2: Trends ---
elif page == "Trends":
    st.title("📈 Sales Trends")
    st.write("### KPIs")
    show_kpis(data)

    sales_by_date = data.groupby("Date")["Sales"].sum()
    fig, ax = plt.subplots()
    sns.lineplot(x=sales_by_date.index, y=sales_by_date.values, marker="o", ax=ax)
    plt.xticks(rotation=45)
    st.pyplot(fig)

# --- Page 3: Summary ---
elif page == "Summary":
    st.title("📑 Summary Report")
    st.write("### KPIs")
    show_kpis(data)

    st.write("### Sales Distribution by Region")
    sales_by_region = data.groupby("Region")["Sales"].sum()
    fig, ax = plt.subplots()
    ax.pie(sales_by_region.values, labels=sales_by_region.index, autopct="%1.1f%%", startangle=90)
    st.pyplot(fig)
