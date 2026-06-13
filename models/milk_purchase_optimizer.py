from models.ensemble_forecast import (
    ensemble_forecast
)


def milk_required(
        cheese_type):

    forecast = (
        ensemble_forecast(
            cheese_type
        )
    )

    pounds_of_milk = (
        forecast * 3.5
    )

    return round(
        pounds_of_milk,
        2
    )