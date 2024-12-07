# Project Title: Gas Price Prediction Project.
    Objective: Describe the goals (e.g., predicting gas prices using regression and time series forecasting).



# Dataset:
    (created a mock data set using some actual public data from https://www.eia.gov/



# Steps to Run:
    1. Preprocess the dataset:
       ```bash
       python3 scripts/preprocess_data.py

       
    2. Train regression model:
        python3 scripts/regression_model.py

        
    3. Train time series model:
        python3 scripts/time_series_model.py


    4. Run the full pipeline:
        python3 scripts/run_pipeline.py

    
# Results 
    1. Highlight key insights from the results.
    
    2. Include the R-squared value from the regression summary.
    
    3. Mention any trends observed in the forecast plot.
    
    4. Optionally, embed images of visualizations: 
        ![Actual vs Predicted](visualizations/actual_vs_predicted_gas_prices.png)
        ![Forecast Plot](visualizations/gas_price_forecast.png)




## Repository Structure

The following is the directory structure of the project:

```plaintext
.
├── data
│   ├── gas_prices.xlsx
│   └── processed_gas_prices.csv
├── notebooks
├── README.md
├── repo_structure.txt
├── requirements.txt
├── results
│   ├── regression_summary.txt
│   └── time_series_summary.txt
├── scripts
│   ├── data_exploration.py
│   ├── plot_results.py
│   ├── preprocess_data.py
│   ├── __pycache__
│   ├── regression_model.py
│   ├── run_pipeline.py
│   └── time_series_model.py
├── venv
│   ├── bin
│   ├── include
│   ├── lib
│   ├── lib64 -> lib
│   ├── pyvenv.cfg
│   └── share
└── visualizations
    ├── actual_vs_predicted_gas_prices.png
    └── gas_price_forecast.png



