import matplotlib.pyplot as plt
import os
import pandas as pd

def plot_gas_prices(data, model, X, output_dir):
    """
    Plot actual vs. predicted gas prices and save the plot to the 'visualizations/' directory.

    Parameters:
    - data (DataFrame): The dataset containing 'date' and 'gas_price' columns.
    - model: The trained regression model with a predict method.
    - X (DataFrame): The features used for prediction.
    - output_dir (str): Path to the directory where the plot will be saved.
    """
    # Create the plot
    plt.figure(figsize=(10, 6))
    plt.plot(data['date'], data['gas_price'], label='Actual Prices', color='blue', linestyle='--', marker='o', alpha=0.7)
    plt.plot(data['date'], model.predict(X), label='Predicted Prices', color='red', linestyle='-', linewidth=2)
    plt.xlabel('Date')
    plt.ylabel('Gas Price')
    plt.title('Actual vs Predicted Gas Prices')
    plt.legend()
    
    # Save the plot
    os.makedirs(output_dir, exist_ok=True)
    plot_path = os.path.join(output_dir, 'actual_vs_predicted_gas_prices.png')
    plt.savefig(plot_path)
    print(f"Plot saved to {plot_path}")
    
    # Show the plot
    plt.show()

if __name__ == "__main__":
    # Example usage
    # Ensure these paths and variables are correctly defined in your project
    data_file = "../data/gas_prices.xls"  # Example data file
    visualizations_dir = "../visualizations"
    
    # Load data (example format)
    data = pd.read_excel(data_file, parse_dates=['date'])
    
    # Placeholder model and features for demonstration
    class MockModel:
        def predict(self, X):
            return X['crude_oil_price'] * 0.5 + X['inflation_rate'] * 0.2  # Mock prediction logic

    model = MockModel()
    features = ['crude_oil_price', 'inflation_rate']
    data['crude_oil_price'] = 100  # Example feature
    data['inflation_rate'] = 2  # Example feature
    X = data[features]
    
    # Plot and save results
    plot_gas_prices(data, model, X, output_dir=visualizations_dir)
