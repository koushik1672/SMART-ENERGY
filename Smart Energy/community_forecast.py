from forecast_horizon import MultiHorizonForecaster

class CommunityEnergyForecaster:
    """
    Scales household-level predictions to community or area-level demand.
    """

    def __init__(self, model_path="model.pkl"):
        self.household_forecaster = MultiHorizonForecaster(model_path)

    def forecast_community(
        self,
        start_hour,
        start_day,
        is_weekend,
        lag_1,
        lag_24,
        hours_ahead,
        number_of_households
    ):
        """
        Predict community-level energy consumption.

        Returns:
        - household_predictions
        - community_predictions
        """

        household_preds = self.household_forecaster.forecast(
            start_hour=start_hour,
            start_day=start_day,
            is_weekend=is_weekend,
            lag_1=lag_1,
            lag_24=lag_24,
            hours_ahead=hours_ahead
        )

        community_preds = [
            pred * number_of_households for pred in household_preds
        ]

        return household_preds, community_preds
