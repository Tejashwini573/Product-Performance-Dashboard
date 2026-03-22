import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")


# 1. Load Dataset

df = pd.read_csv("Chocolate Sales (2).csv")
df.head()
df.describe()
df.info()
print(df.columns)

# 2. Data Cleaning


# Remove extra spaces from column names
df.columns = df.columns.str.strip()

# Convert Date column
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

# Clean Amount column ($ and commas)
df['Amount'] = df['Amount'].replace('[\$,]', '', regex=True).astype(float)

# Ensure numeric
df['Boxes Shipped'] = pd.to_numeric(df['Boxes Shipped'], errors='coerce')

# Create Month column
df['Month'] = df['Date'].dt.to_period('M')

print("\nCleaned Data:")
print(df.head())


# 3. KPI Calculations


total_sales = df['Amount'].sum()
total_boxes = df['Boxes Shipped'].sum()
total_orders = len(df)

print("\n===== KPI RESULTS =====")
print("Total Revenue:", round(total_sales,2))
print("Total Boxes Shipped:", total_boxes)
print("Total Orders:", total_orders)


# 4. Sales by Product


product_sales = df.groupby('Product')['Amount'].sum().sort_values(ascending=False)

plt.figure()
product_sales.plot(kind='bar')
plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 5. Sales by Country

country_sales = df.groupby('Country')['Amount'].sum()

plt.figure()
country_sales.plot(kind='pie', autopct='%1.1f%%')
plt.title("Sales Distribution by Country")
plt.ylabel("")
plt.show()

# 6. Monthly Sales Trend

monthly_sales = df.groupby('Month')['Amount'].sum()

plt.figure()
monthly_sales.plot(marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# 7. Boxes Shipped by Product

boxes_product = df.groupby('Product')['Boxes Shipped'].sum()

plt.figure()
sns.barplot(x=boxes_product.index, y=boxes_product.values)
plt.title("Boxes Shipped by Product")
plt.xlabel("Product")
plt.ylabel("Boxes Shipped")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# 8. Top Salespersons

salesperson_sales = df.groupby('Sales Person')['Amount'].sum().sort_values(ascending=False)

plt.figure()
salesperson_sales.head(10).plot(kind='bar')
plt.title("Top 10 Salespersons by Revenue")
plt.xlabel("Sales Person")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# 9. Sales vs Boxes Shipped

plt.figure()
sns.scatterplot(data=df, x='Boxes Shipped', y='Amount', hue='Product')
plt.title("Sales vs Boxes Shipped")
plt.tight_layout()
plt.show()

df.to_csv("chocolate_sales_cleaned.csv")
print("\n✅ Data Analysis Completed Successfully!")
