import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv("raw_customer_data.csv")

print("===== ORIGINAL DATA =====")
print(df)

# Store original row count
before_rows = len(df)

# Remove duplicate rows
df = df.drop_duplicates()

# Fill missing Age values
df["Age"] = df["Age"].fillna(df["Age"].mean())

# Fill missing PurchaseAmount values
df["PurchaseAmount"] = df["PurchaseAmount"].fillna(
    df["PurchaseAmount"].mean()
)

# Standardize City names
df["City"] = df["City"].str.title()

# Convert dates
df["PurchaseDate"] = pd.to_datetime(
    df["PurchaseDate"],
    errors="coerce",
    dayfirst=True
)

# Save cleaned data as CSV
df.to_csv(
    "cleaned_customer_data.csv",
    index=False
)

# Save cleaned data as Excel
df.to_excel(
    "cleaned_customer_data.xlsx",
    index=False
)

print("\n===== CLEANED DATA =====")
print(df)

print("\nData Cleaning Completed Successfully!")

# Graph
after_rows = len(df)

plt.bar(
    ["Before Cleaning", "After Cleaning"],
    [before_rows, after_rows]
)

plt.title("Dataset Size Comparison")
plt.ylabel("Number of Rows")

# Project Summary
print("\n===== PROJECT SUMMARY =====")

print("Rows Before Cleaning :", before_rows)
print("Rows After Cleaning  :", after_rows)

print("Duplicates Removed   :", before_rows - after_rows)

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

plt.show()