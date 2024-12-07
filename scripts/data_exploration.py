import pandas as pd

# Load dataset
try:
    # Update to read an Excel file instead of a CSV
    data = pd.read_excel('data/gas_prices.xlsx')  # Use pd.read_excel for Excel files
    print("Dataset successfully loaded.")
except FileNotFoundError:
    print("Error: The dataset file 'gas_prices.xlsx' was not found in the 'data/' directory.")
    exit()
except Exception as e:
    print(f"An unexpected error occurred while loading the dataset: {e}")
    exit()

# Display the first few rows
print("\n### First 5 Rows of the Dataset ###")
print(data.head())

# General information about the dataset
print("\n### Dataset Information ###")
print(data.info())

# Statistical summary of numerical columns
print("\n### Summary Statistics ###")
print(data.describe(include='all'))  # Includes categorical data if present

# Check for missing values
print("\n### Missing Values Per Column ###")
print(data.isnull().sum())

# Check for duplicate rows
duplicates = data.duplicated().sum()
print(f"\n### Number of Duplicate Rows: {duplicates} ###")

if duplicates > 0:
    print("Consider removing duplicates for cleaner analysis.")

# Inspect column names
print("\n### Column Names ###")
print(data.columns)

# Data type analysis
print("\n### Column Data Types ###")
print(data.dtypes)

# Output data shape
print("\n### Dataset Shape ###")
print(f"Number of rows: {data.shape[0]}")
print(f"Number of columns: {data.shape[1]}")


