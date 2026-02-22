import pandas as pd

data = pd.read_csv(
    "household_power_consumption.txt",
    sep=";",
    na_values=["?"],
    low_memory=False
)

print("Data loaded successfully")
print(data.head())

