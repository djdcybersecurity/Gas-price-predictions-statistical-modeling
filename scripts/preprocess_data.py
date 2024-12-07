import pandas as pd

def preprocess_data(file_path):
    """
    Load, clean, and save the processed dataset.
    """
    try:
        # Load dataset
        data = pd.read_excel(file_path)
        print("Dataset loaded successfully.")

        # Remove duplicates
        data = data.drop_duplicates()

        # Handle missing values (example: drop rows with missing data)
        data = data.dropna()

        # Save cleaned dataset
        output_path = "../data/processed_gas_prices.csv"
        data.to_csv(output_path, index=False)
        print(f"Cleaned data saved to {output_path}")
        return data
    except FileNotFoundError:
        print(f"Error: The dataset file '{file_path}' was not found.")
        exit()
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
        exit()

if __name__ == "__main__":
    # Path to the raw dataset
    preprocess_data("../data/gas_prices.xlsx")

