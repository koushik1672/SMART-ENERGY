import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error

print("Training Random Forest model...")

# Load dataset
data = pd.read_csv(
    "household_power_consumption.txt",
    sep=";",
    na_values=["?"],
    low_memory=False
)

# DateTime index
data["DateTime"] = pd.to_datetime(
    data["Date"] + " " + data["Time"],
    format="%d/%m/%Y %H:%M:%S"
)
data.set_index("DateTime", inplace=True)

# Keep target
data = data[["Global_active_power"]]
data.dropna(inplace=True)

# Hourly resampling
hourly_data = data.resample("h").mean()

# Feature engineering
hourly_data["hour"] = hourly_data.index.hour
hourly_data["day_of_week"] = hourly_data.index.dayofweek
hourly_data["is_weekend"] = (hourly_data["day_of_week"] >= 5).astype(int)
hourly_data["lag_1"] = hourly_data["Global_active_power"].shift(1)
hourly_data["lag_24"] = hourly_data["Global_active_power"].shift(24)
hourly_data.dropna(inplace=True)

# Train-test split (time-based)
X = hourly_data.drop(columns=["Global_active_power"])
y = hourly_data["Global_active_power"]

split_index = int(len(hourly_data) * 0.8)

X_train = X.iloc[:split_index]
X_test = X.iloc[split_index:]
y_train = y.iloc[:split_index]
y_test = y.iloc[split_index:]

# 🔹 RANDOM FOREST MODEL
rf_model = RandomForestRegressor(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)

rf_model.fit(X_train, y_train)

print("Random Forest training completed")

# Prediction
y_pred = rf_model.predict(X_test)

# Evaluation
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print("\nRandom Forest Evaluation:")
print("MAE :", round(mae, 4))
print("RMSE:", round(rmse, 4))
