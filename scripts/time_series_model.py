import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt
import os


def train_arima_model(file_path):
    """
    Train an ARIMA model to forecast gas prices.
    """
    try:
        # Load the dataset and parse dates
        data = pd.read_csv(file_path, parse_dates=["Date"], index_col="Date")
        print("Dataset loaded successfully with the Date column as index.")

        # Train the ARIMA model
        model = ARIMA(data["Gas_Price"], order=(1, 1, 1))
        model_fit = model.fit()

        # Save model summary
        with open("../results/time_series_summary.txt", "w") as f:
            f.write(model_fit.summary().as_text())
        print("Time series model summary saved to '../results/time_series_summary.txt'.")

        # Forecast gas prices
        forecast = model_fit.forecast(steps=12)

        # Plot the forecast
        output_path = "../visualizations/gas_price_forecast.png"
        plot_forecast(data["Gas_Price"], forecast, output_path)

        return model_fit
    except FileNotFoundError:
        print(f"Error: The dataset file '{file_path}' was not found.")
        exit()
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
        exit()


def plot_forecast(actual, forecast, output_path):
    """
    Generate and save a plot showing the actual vs forecasted gas prices.
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    plt.figure(figsize=(10, 6))
    plt.plot(actual.index, actual, label="Actual Prices")
    plt.plot(forecast.index, forecast, label="Forecasted Prices", color="red")
    plt.legend()
    plt.xlabel("Date")
    plt.ylabel("Gas Price")
    plt.title("Gas Price Forecast")
    plt.savefig(output_path)
    print(f"Forecast plot saved to {output_path}")
    plt.close()


if __name__ == "__main__":
    train_arima_model("../data/processed_gas_prices.csv")
