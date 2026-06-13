from models.demand_forecast import (
    forecast_cheese_demand
)

from models.xgboost_forecast import (
    xgboost_forecast
)


def ensemble_forecast(
        cheese_type):

    prophet_prediction = (
        forecast_cheese_demand(
            cheese_type
        )
    )

    xgb_prediction = (
        xgboost_forecast(
            cheese_type
        )
    )

    prediction = int(
        (
            prophet_prediction
            + xgb_prediction
        ) / 2
    )

    return prediction