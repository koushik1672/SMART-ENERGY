import pandas as pd

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
data = data[["Global_active_power"]]
data.dropna(inplace=True)

hourly = data.resample("h").mean()

print("Hourly resampling done")
print(hourly.head())

