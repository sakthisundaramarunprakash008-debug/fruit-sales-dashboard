import pandas as pd

# Load dataset
data = pd.read_csv("sales.csv")

# Handle missing values
data["Sales"] = data["Sales"].fillna(data["Sales"].mean())

# Rename columns
data = data.rename(columns={"Product": "Item", "Sales": "Units_Sold"})

# Convert Date column to datetime
data["Date"] = pd.to_datetime(data["Date"])

print(data.head())
