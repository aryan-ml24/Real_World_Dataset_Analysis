import pandas as pd

df = pd.read_csv("cleaned_dataset.csv")

print("=" * 50)
print("REAL-WORLD SALES DATA ANALYSIS")
print("=" * 50)

print("\nTOTAL SALES:")
print(round(df["Sales"].sum(), 2))

print("\nTOTAL PROFIT:")
print(round(df["Profit"].sum(), 2))

print("\nSALES BY CATEGORY:")
print(df.groupby("Category")["Sales"].sum().sort_values(ascending=False))

print("\nPROFIT BY CATEGORY:")
print(df.groupby("Category")["Profit"].sum().sort_values(ascending=False))

print("\nSALES BY REGION:")
print(df.groupby("Region")["Sales"].sum().sort_values(ascending=False))

print("\nPROFIT BY REGION:")
print(df.groupby("Region")["Profit"].sum().sort_values(ascending=False))

print("\nTOP 10 PRODUCTS BY SALES:")
print(df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10))

print("\nLOSS-MAKING ROWS:")
print((df["Profit"] < 0).sum())

print("\nAVERAGE SALES:")
print(round(df["Sales"].mean(), 2))

print("\nAVERAGE PROFIT:")
print(round(df["Profit"].mean(), 2))

print("\nANALYSIS COMPLETED SUCCESSFULLY!")
