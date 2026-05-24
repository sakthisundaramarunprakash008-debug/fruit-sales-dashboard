import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("sales.csv")

# Group by Product and sum Sales
sales_by_product = data.groupby("Product")["Sales"].sum()

# Plot bar chart
sales_by_product.plot(kind="bar", color=["blue", "green", "pink"])
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.show()
