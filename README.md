# XAUUSD Intraday Price Prediction

This project provides a Python script that predicts the intraday close price of XAUUSD (Gold futures) using a machine learning model. The script fetches real-time data from Yahoo Finance, trains an XGBoost regression model on the most recent intervals, and predicts the close price for the current interval. The results are then plotted to compare the predicted close price with the actual close price.

## Table of Contents - [Installation](#installation) - [Usage](#usage) - [Features](#features) - [Requirements](#requirements) - [License](#license)

## Installation

To get started with this project, you need to have Python installed on your machine. You can clone this repository and install the required dependencies using pip.

```bash git clone https://github.com/yourusername/xauusd_price_prediction.git cd xauusd_price_prediction pip install -r requirements.txt ```

If the `requirements.txt` file is not available, you can manually install the required packages:

```bash pip install yfinance pandas xgboost matplotlib scikit-learn ```

## Usage

Once you have installed the required packages, you can run the script to fetch real-time data, train the model, and predict the close price. The script will:

1. Fetch real-time intraday data for XAUUSD from Yahoo Finance. 2. Display the fetched data. 3. Train an XGBoost regression model on the last 10 intervals. 4. Predict the close price for the current interval. 5. Compare the predicted close price to the actual close price (if available). 6. Plot the actual vs predicted close prices.

## Features

- **Real-time Data Fetching**: The script fetches intraday data for XAUUSD with a 1-minute interval. - **Machine Learning Prediction**: Uses XGBoost, a powerful machine learning model, to predict the close price based on recent data. - **Visualization**: Plots the actual vs predicted close prices for easy comparison. - **Customizable**: You can easily modify the script to adjust the number of intervals used for training or the features used for prediction.

## Requirements

- Python 3.x - yfinance - pandas - xgboost - matplotlib - scikit-learn

You can install all the required dependencies using pip as mentioned in the installation section.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

This project uses data from Yahoo Finance and leverages the power of XGBoost for machine learning predictions. --- Feel free to contribute to this project by submitting issues or pull requests. If you have any questions, you can contact me at https://satoshialpha.com/.
