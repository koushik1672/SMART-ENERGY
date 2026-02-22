import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

print("Preparing data for visualization...")

# Load and preprocess data
data = pd.read_csv(
    "household_power_consumption.txt",
    sep=";",
    na_values=["?"],
    low_memory=False
)

data["DateTime"] = pd.to_datetime(
    data["Date"] + " " + data["Time"],
    format="%d/%m/%Y %H:%M:%S"
)
data.set_index("DateTime", inplace=True)

data.drop(columns=["Date", "Time"], inplace=True)
data = data[["Global_active_power"]]
data.dropna(inplace=True)

# Resample to hourly
hourly_data = data.resample("h").mean()

# Feature engineering
hourly_data["hour"] = hourly_data.index.hour
hourly_data["day_of_week"] = hourly_data.index.dayofweek
hourly_data["is_weekend"] = (hourly_data["day_of_week"] >= 5).astype(int)
hourly_data["lag_1"] = hourly_data["Global_active_power"].shift(1)
hourly_data["lag_24"] = hourly_data["Global_active_power"].shift(24)
hourly_data.dropna(inplace=True)

# Train-test split
X = hourly_data.drop(columns=["Global_active_power"])
y = hourly_data["Global_active_power"]

split_index = int(len(hourly_data) * 0.8)

X_train = X.iloc[:split_index]
X_test = X.iloc[split_index:]
y_train = y.iloc[:split_index]
y_test = y.iloc[split_index:]

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# 🔹 VISUALIZATION
plt.figure(figsize=(12, 5))
plt.plot(y_test.values[:200], label="Actual")
plt.plot(y_pred[:200], label="Predicted")
plt.title("Actual vs Predicted Energy Consumption (First 200 Hours)")
plt.xlabel("Time (hours)")
plt.ylabel("Global Active Power (kW)")
plt.legend()
plt.tight_layout()
plt.show()
