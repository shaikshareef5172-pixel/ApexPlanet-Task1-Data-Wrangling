# ApexPlanet-Task1-Data-Wrangling
ApexPlanet Data Analytics Internship - Task 1: Data Immersion and Wrangling using Python and Pandas.

## Project Objective

The objective of this project is to understand, assess, clean, transform, and prepare a sales dataset for further data analysis.

## Dataset

The project uses the provided ApexPlanet sales dataset.

Original dataset:

- 1,000 rows
- 12 columns

## Dataset Columns

- Order_ID
- Order_Date
- Customer_ID
- Customer_Name
- Age
- Gender
- City
- Product
- Category
- Quantity
- Unit_Price
- Total_Sales

## Data Quality Assessment

The dataset was checked for:

- Missing values
- Duplicate records
- Duplicate Order IDs
- Invalid numerical values
- Data type consistency
- Statistical outliers
- Sales calculation consistency

## Findings

- 20 missing Age values
- 13 missing City values
- 8 repeated Order_ID records
- 0 exact duplicate rows
- No non-positive Quantity values
- No non-positive Unit_Price values
- No non-positive Total_Sales values
- 19 statistical outliers were identified in Total_Sales using the IQR method

The Total_Sales outliers were retained because an outlier is not automatically a data error.

## Data Cleaning

The following operations were performed:

1. Standardized column names.
2. Removed unnecessary spaces from text fields.
3. Converted Order_Date to datetime.
4. Filled missing Age values using the median.
5. Filled missing City values using the mode.
6. Removed repeated Order_ID records, keeping the first occurrence.
7. Removed exact duplicate rows.
8. Checked invalid numerical values.
9. Validated Total_Sales against Quantity × Unit_Price.
10. Created Order_Year.
11. Created Order_Month.
12. Created Order_Month_Name.

## Final Dataset

After cleaning:

- 992 rows
- 15 columns

## Tools Used

- Python
- Pandas
- NumPy
- OpenPyXL
- Visual Studio Code

## Project Structure

```text
ApexPlanet_Task1_Data_Wrangling/
│
├── README.md
├── requirements.txt
│
├── data/
│   ├── raw/
│   └── processed/
│
├── reports/
│
├── src/
│
└── docs/
