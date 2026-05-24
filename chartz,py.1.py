import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv("sales.csv")

# --- Chart Functions ---

def plot_bar_chart(data):
    sales_by_product = data.groupby("Product")["Sales"].sum()
    plt.figure(figsize=(6,4))
    sns.barplot(x=sales_by_product.index, y=sales_by_product.values, palette="viridis")
    plt.title("Total Sales by Product")
    plt.xlabel("Product")
    plt.ylabel("Sales")
    plt.show()

def plot_line_chart(data):
    sales_by_date = data.groupby("Date")["Sales"].sum()
    plt.figure(figsize=(6,4))
    sns.lineplot(x=sales_by_date.index, y=sales_by_date.values, marker="o")
    plt.title("Sales Trend Over Time")
    plt.xlabel("Date")
    plt.ylabel("Sales")
    plt.xticks(rotation=45)
    plt.show()

def plot_pie_chart(data):
    sales_by_region = data.groupby("Region")["Sales"].sum()
    plt.figure(figsize=(6,6))
    plt.pie(sales_by_region.values, labels=sales_by_region.index, autopct="%1.1f%%", startangle=90)
    plt.title("Sales Distribution by Region")
    plt.show()

# --- Example Usage ---
if __name__ == "__main__":
    plot_bar_chart(data)
    plot_line_chart(data)
    plot_pie_chart(data)
