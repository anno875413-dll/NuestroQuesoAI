import pandas as pd
from prophet import Prophet


def forecast_cheese_demand(cheese_type):

    df = pd.read_csv("data/historical_sales.csv")

    df = df[df["cheese_type"] == cheese_type]

    df = df.rename(
        columns={
            "date": "ds",
            "units_sold": "y"
        }
    )

    model = Prophet(
        yearly_seasonality=True,
        weekly_seasonality=True,
        daily_seasonality=False
    )

    model.fit(df)

    future = model.make_future_dataframe(periods=30)

    forecast = model.predict(future)

    predicted_units = int(
        forecast["yhat"].tail(30).sum()
    )

    return predicted_units