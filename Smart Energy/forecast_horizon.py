import joblib
import numpy as np

class MultiHorizonForecaster:
    """
    This class performs multi-step (hourly) forecasting
    using an already trained one-step ML model.
    """

    def __init__(self, model_path="model.pkl"):
        self.model = joblib.load(model_path)

    def forecast(
        self,
        start_hour,
        start_day,
        is_weekend,
        lag_1,
        lag_24,
        hours_ahead=24
    ):
        """
        Predict energy consumption for multiple future hours.

        Parameters:
        - start_hour (int): current hour (0–23)
        - start_day (int): day of week (0=Mon, 6=Sun)
        - is_weekend (int): 1 if weekend, else 0
        - lag_1 (float): last known hour consumption
        - lag_24 (float): same hour previous day consumption
        - hours_ahead (int): number of future hours to predict

        Returns:
        - list of predicted values
        """

        predictions = []

        current_hour = start_hour
        current_day = start_day
        current_lag_1 = lag_1
        current_lag_24 = lag_24

        for step in range(hours_ahead):
            input_data = np.array([[
                current_hour,
                current_day,
                is_weekend,
                current_lag_1,
                current_lag_24
            ]])

            pred = self.model.predict(input_data)[0]
            predictions.append(pred)

            # Update lags for next step
            current_lag_1 = pred

            # Advance hour
            current_hour += 1
            if current_hour == 24:
                current_hour = 0
                current_day = (current_day + 1) % 7
                is_weekend = 1 if current_day >= 5 else 0
                current_lag_24 = pred  # approximate daily lag update

        return predictions
