from preprocess_data import preprocess_data
from regression_model import train_regression_model
from time_series_model import train_arima_model

def main():
    # Preprocess the dataset
    preprocess_data("../data/gas_prices.xlsx")

    # Train and evaluate the regression model
    train_regression_model("../data/processed_gas_prices.csv")

    # Train and evaluate the time series model
    train_arima_model("../data/processed_gas_prices.csv")

if __name__ == "__main__":
    main()



