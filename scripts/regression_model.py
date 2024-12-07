import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import os


def train_regression_model(file_path):
    """
    Train a regression model to predict gas prices.
    """
    try:
        # Load the processed dataset
        data = pd.read_csv(file_path)
        print("Processed dataset loaded successfully.")

        # Define features and target variable
        features = ["Crude_Oil_Price", "Inflation_Rate", "Unemployment_Rate"]
        target = "Gas_Price"

        X = data[features]
        y = data[target]

        # Add a constant for the regression model
        X = sm.add_constant(X)

        # Train the regression model
        model = sm.OLS(y, X).fit()

        # Save model summary
        with open("../results/regression_summary.txt", "w") as f:
            f.write(model.summary().as_text())
        print("Regression model summary saved to '../results/regression_summary.txt'.")

        return model, X, y
    except FileNotFoundError:
        print(f"Error: The dataset file '{file_path}' was not found.")
        exit()
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
        exit()


def plot_actual_vs_predicted(y, y_pred, output_path):
    """
    Generate and save a plot comparing actual and predicted gas prices.
    """
    # Create visualizations directory if it doesn't exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    plt.figure(figsize=(10, 6))
    plt.scatter(range(len(y)), y, label="Actual Prices", alpha=0.7)
    plt.plot(range(len(y_pred)), y_pred, label="Predicted Prices", color="red", alpha=0.7)
    plt.legend()
    plt.xlabel("Index")
    plt.ylabel("Gas Price")
    plt.title("Actual vs Predicted Gas Prices")
    plt.savefig(output_path)  # Save the plot
    print(f"Plot saved to {output_path}")
    plt.close()  # Close the plot


if __name__ == "__main__":
    # Train the regression model
    model, X, y = train_regression_model("../data/processed_gas_prices.csv")

    # Generate predictions
    y_pred = model.predict(X)

    # Save the plot
    output_path = "../visualizations/actual_vs_predicted_gas_prices.png"
    plot_actual_vs_predicted(y, y_pred, output_path)



