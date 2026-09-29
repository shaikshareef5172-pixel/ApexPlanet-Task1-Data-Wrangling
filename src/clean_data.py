import pandas as pd
import numpy as np
from pathlib import Path

# -----------------------------
# 1. File locations
# -----------------------------
BASE_DIR = Path(__file__).resolve().parents[1]
INPUT_FILE = BASE_DIR / "data" / "raw" / "ApexPlanet_DataAnalytics_Dataset.xlsx"
OUTPUT_DIR = BASE_DIR / "data" / "processed"
OUTPUT_FILE = OUTPUT_DIR / "cleaned_sales_dataset.csv"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# -----------------------------
# 2. Read Excel dataset
# -----------------------------
df = pd.read_excel(INPUT_FILE, sheet_name="Sales_Dataset")

print("Original shape:", df.shape)
print("\nOriginal columns:")
print(df.columns.tolist())

# -----------------------------
# 3. Clean text columns
# -----------------------------
text_cols = [
    "Order_ID", "Customer_ID", "Customer_Name",
    "Gender", "City", "Product", "Category"
]

for col in text_cols:
    df[col] = df[col].astype("string").str.strip()

# -----------------------------
# 4. Convert date
# -----------------------------
df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")

# -----------------------------
# 5. Handle missing values
# -----------------------------
median_age = df["Age"].median()
df["Age"] = df["Age"].fillna(median_age)
df["City"] = df["City"].fillna("Unknown")

# -----------------------------
# 6. Create unique row ID
# -----------------------------
df["Record_ID"] = range(1, len(df) + 1)

# Flag repeated Order_IDs instead of deleting them
order_counts = df["Order_ID"].value_counts(dropna=False)
df["Order_ID_Duplicate_Flag"] = df["Order_ID"].map(order_counts).gt(1)

# -----------------------------
# 7. Validate Total_Sales
# -----------------------------
df["Total_Sales_Calculated"] = (
    df["Quantity"] * df["Unit_Price"]
).round(2)

df["Sales_Check"] = np.isclose(
    df["Total_Sales"],
    df["Total_Sales_Calculated"],
    atol=0.01
)

# -----------------------------
# 8. Feature engineering
# -----------------------------
df["Order_Year"] = df["Order_Date"].dt.year
df["Order_Month"] = df["Order_Date"].dt.month
df["Order_Month_Name"] = df["Order_Date"].dt.month_name()

df["Age_Group"] = pd.cut(
    df["Age"],
    bins=[17, 25, 35, 45, 55, 65],
    labels=["18-25", "26-35", "36-45", "46-55", "56-65"],
    include_lowest=True
)

# -----------------------------
# 9. Final quality checks
# -----------------------------
print("\nMissing values after cleaning:")
print(df.isna().sum())

print("\nFully duplicated rows:", df.duplicated().sum())
print("Repeated Order_ID rows:", df["Order_ID"].duplicated(keep=False).sum())
print("Sales checks passed:", df["Sales_Check"].sum(), "/", len(df))

# -----------------------------
# 10. Save analysis-ready data
# -----------------------------
df["Order_Date"] = df["Order_Date"].dt.strftime("%Y-%m-%d")
df.to_csv(OUTPUT_FILE, index=False)

print("\nCleaned dataset saved to:")
print(OUTPUT_FILE)
