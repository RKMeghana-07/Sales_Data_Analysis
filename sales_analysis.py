import pandas as pd

# CSV
df = pd.read_csv("sales_data.csv")
print("CSV loaded successfully")
print("-" * 50)

# Check
print("First 5 rows:")
print(df.head())
print("-" * 50)

print("Last 5 rows:")
print(df.tail())
print("-" * 50)

print("Shape (rows, columns):")
print(df.shape)
print("-" * 50)

print("Column names:")
print(df.columns)
print("-" * 50)

print("Info:")
print(df.info())
print("-" * 50)

# Stats
print("Summary statistics (numeric columns):")
print(df.describe())
print("-" * 50)

total_revenue = df["Total"].sum()
avg_bill = df["Total"].mean()
max_bill = df["Total"].max()
min_bill = df["Total"].min()

print("TOTAL REVENUE:", total_revenue)
print("AVERAGE BILL:", avg_bill)
print("HIGHEST BILL:", max_bill)
print("LOWEST BILL:", min_bill)
print("-" * 50)

# Filter
high_value_orders = df[df["Total"] > 500]
print("High-value orders (Total > 500):")
print(high_value_orders.head())
print("-" * 50)

example_city = df["City"].iloc[0]
city_orders = df[df["City"] == example_city]
print(f"Orders from {example_city}:")
print(city_orders.head())
print("-" * 50)


sales_by_city = df.groupby("City")["Total"].sum().sort_values(ascending=False)
print("Total Sales by City:")
print(sales_by_city)
print("-" * 50)

sales_by_product = df.groupby("Product line")["Total"].sum().sort_values(ascending=False)
print("Total Sales by Product Line:")
print(sales_by_product)
print("-" * 50)

# Save
high_value_orders.to_csv("high_value_orders.csv", index=False)
sales_by_city.reset_index().to_csv("sales_by_city.csv", index=False)
sales_by_product.reset_index().to_csv("sales_by_product_line.csv", index=False)

print("Files exported:")
print(" 1. high_value_orders.csv")
print(" 2. sales_by_city.csv")
print(" 3. sales_by_product_line.csv")
print("-" * 50)
print("Analysis completed!")

