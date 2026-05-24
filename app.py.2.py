import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# --- Load Dataset ---
data = pd.read_csv("sales.csv")
data["Date"] = pd.to_datetime(data["Date"])  # ensure datetime

# --- Sidebar Navigation ---
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Sales", "Trends", "Summary"])

# --- Date Range Filter ---
st.sidebar.write("### Date Range")
start_date = st.sidebar.date_input("Start Date", data["Date"].min())
end_date = st.sidebar.date_input("End Date", data["Date"].max())

filtered_data = data[(data["Date"] >= pd.to_datetime(start_date)) & (data["Date"] <= pd.to_datetime(end_date))]

# --- KPI Function ---
def show_kpis(df):
    st.write("### KPIs")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Sales", f"{df['Sales'].sum():,.0f}")
    col2.metric("Average Sales", f"{df['Sales'].mean():,.2f}")
    col3.metric("Records", len(df))

# --- Export Button ---
def export_data(df):
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="⬇️ Download Filtered Data",
        data=csv,
        file_name="filtered_sales.csv",
        mime="text/csv"
    )

# --- Sales Page ---
if page == "Sales":
    st.title("📊 Sales Dashboard")
    show_kpis(filtered_data)
    st.dataframe(filtered_data)
    export_data(filtered_data)

    st.write("### Sales by Product")
    sales_by_product = filtered_data.groupby("Product")["Sales"].sum()
    fig, ax = plt.subplots()
    sns.barplot(x=sales_by_product.index, y=sales_by_product.values, ax=ax, palette="viridis")
    st.pyplot(fig)

# --- Trends Page ---
elif page == "Trends":
    st.title("📈 Sales Trends")
    show_kpis(filtered_data)
    export_data(filtered_data)

    sales_by_date = filtered_data.groupby("Date")["Sales"].sum()
    fig, ax = plt.subplots()
    sns.lineplot(x=sales_by_date.index, y=sales_by_date.values, marker="o", ax=ax)
    plt.xticks(rotation=45)
    st.pyplot(fig)

# --- Summary Page ---
elif page == "Summary":
    st.title("📑 Summary Report")
    show_kpis(filtered_data)
    export_data(filtered_data)

    st.write("### Sales Distribution by Region")
    sales_by_region = filtered_data.groupby("Region")["Sales"].sum()
    fig, ax = plt.subplots()
    ax.pie(sales_by_region.values, labels=sales_by_region.index, autopct="%1.1f%%", startangle=90)
    st.pyplot(fig)
