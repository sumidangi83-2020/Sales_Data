import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create the Sales Data
data = {
    "Date": pd.date_range(start="2025-01-01", periods=10, freq="D"),
    "Product": ["Laptop", "Phone", "Tablet", "Laptop", "Phone", "Tablet", "Laptop", "Phone", "Tablet", "Laptop"],
    "Quantity": [5, 10, 7, 8, 6, 3, 12, 15, 9, 4],
    "Price": [70000, 30000, 20000, 75000, 32000, 21000, 72000, 31000, 22000, 76000]
}

df = pd.DataFrame(data)

# Save to CSV file
df.to_csv("sales_data.csv", index=False)

print("Sample sales data created and saved to 'sales_data.csv'")
print(df)




# open CSV file and read
df = pd.read_csv("sales_data.csv")

print("\nFirst 5 rows ---- ")
print(df.head())

print("\nInfo of Data ----" )
print(df.info())

print("\nSummary ----" )
print(df.describe())




# Total Revenue  & column add 
df["Revenue"] = df["Quantity"] * df["Price"]
print("\n=== Data with Revenue ===")
print(df)

# Total revenue calculation
total_revenue = df["Revenue"].sum()
print(f"\nTotal Revenue: ₹{total_revenue}")

# Product-wise sales summary
print("\n=== Revenue by Product ===")
print(df.groupby("Product")["Revenue"].sum())




# Product-wise Revenue Chart
product_revenue = df.groupby("Product")["Revenue"].sum()

plt.figure(figsize=(8, 5))
product_revenue.plot(kind="bar", color="skyblue", edgecolor="black")
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue (₹)")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()

