import yfinance as yf
import pandas as pd
import xgboost as xgb
import matplotlib.pyplot as plt

# Fetch real-time data for XAUUSD (Gold futures)
data = yf.download(tickers='GC=F', period='1d', interval='1m')

# Display the fetched data
print("Fetched real-time intraday data:")
print(data.head())

# Use the last 10 intervals for training
train_data = data.iloc[-11:-1]  # Last 10 intervals for training
predict_data = data.iloc[-1:]   # The most recent data for prediction

# Define features and target
features = ['Open', 'High', 'Low', 'Volume']
target = 'Close'

# Train the model on the last 10 intervals
model = xgb.XGBRegressor()
model.fit(train_data[features], train_data[target])

# Predict the close price for the current interval
predicted_close = model.predict(predict_data[features])
print(f"\nPredicted Close Price for the current interval: {predicted_close[0]}")

# Compare to actual close price if available
actual_close = predict_data[target].values[0]
print(f"Actual Close Price for the current interval: {actual_close}")

# Plot the actual vs predicted price
plt.plot(predict_data.index, [actual_close], label="Actual Close Price", marker='o')
plt.plot(predict_data.index, predicted_close, label="Predicted Close Price", color='orange', marker='x')
plt.title("XAUUSD Actual vs Predicted Close Price for the Current Interval")
plt.xlabel("Time")
plt.ylabel("Close Price")
plt.legend()
plt.show()