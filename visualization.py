import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create graphs folder
os.makedirs("graphs", exist_ok=True)

# Load cleaned dataset
df = pd.read_csv("cleaned_dataset.csv")

sns.set_theme(style="whitegrid")

# Graph 1: Category-wise Sales
plt.figure(figsize=(8, 5))
df.groupby("Category")["Sales"].sum().plot(kind="bar")
plt.title("Sales by Product Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("graphs/category_sales.png")
plt.show()

# Graph 2: Region-wise Profit
plt.figure(figsize=(8, 5))
df.groupby("Region")["Profit"].sum().plot(kind="bar")
plt.title("Profit by Region")
plt.xlabel("Region")
plt.ylabel("Total Profit")
plt.tight_layout()
plt.savefig("graphs/region_profit.png")
plt.show()

# Graph 3: Monthly Sales Trend
df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")

monthly_sales = (
    df.dropna(subset=["Order Date"])
      .set_index("Order Date")["Sales"]
      .resample("MS")
      .sum()
)

plt.figure(figsize=(12, 5))
plt.plot(monthly_sales.index, monthly_sales.values, marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("graphs/monthly_sales.png")
plt.show()

# Graph 4: Sales Distribution
plt.figure(figsize=(8, 5))
sns.histplot(df["Sales"], bins=40, kde=True)
plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.tight_layout()
plt.savefig("graphs/sales_distribution.png")
plt.show()

# Graph 5: Sales vs Profit
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="Sales", y="Profit", hue="Category", alpha=0.6)
plt.title("Sales vs Profit")
plt.tight_layout()
plt.savefig("graphs/sales_vs_profit.png")
plt.show()

# Graph 6: Correlation Heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(
    df.select_dtypes(include="number").corr(),
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("graphs/correlation_heatmap.png")
plt.show()

print("All 6 graphs created successfully!")
print("Check the graphs folder.")