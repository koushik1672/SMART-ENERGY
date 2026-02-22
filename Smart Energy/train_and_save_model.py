import pandas as pd
import joblib
from sklearn.ensemble import GradientBoostingRegressor

print("Training and saving model...")

# Load data
data = pd.read_csv(
    "household_power_consumption.txt",
    sep=";",
    na_values=["?"],
    low_memory=False
)

# DateTime
data["DateTime"] = pd.to_datetime(
    data["Date"] + " " + data["Time"],
    format="%d/%m/%Y %H:%M:%S"
)
data.set_index("DateTime", inplace=True)

# Target
data = data[["Global_active_power"]]
data.dropna(inplace=True)

# Hourly
hourly = data.resample("h").mean()

# Features
hourly["hour"] = hourly.index.hour
hourly["day_of_week"] = hourly.index.dayofweek
hourly["is_weekend"] = (hourly["day_of_week"] >= 5).astype(int)
hourly["lag_1"] = hourly["Global_active_power"].shift(1)
hourly["lag_24"] = hourly["Global_active_power"].shift(24)
hourly.dropna(inplace=True)

X = hourly.drop(columns=["Global_active_power"])
y = hourly["Global_active_power"]

# Train model
model = GradientBoostingRegressor(
    n_estimators=150,
    learning_rate=0.05,
    max_depth=3,
    random_state=42
)
model.fit(X, y)

# Save model
joblib.dump(model, "model.pkl")
print("Model saved as model.pkl")
