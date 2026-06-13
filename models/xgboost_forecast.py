import pandas as pd
from xgboost import XGBRegressor


def xgboost_forecast(cheese_type):

    df = pd.read_csv(
        "data/historical_sales.csv"
    )

    df = df[
        df["cheese_type"] == cheese_type
    ].copy()

    df["date"] = pd.to_datetime(df["date"])

    df["day"] = df["date"].dt.day
    df["month"] = df["date"].dt.month
    df["weekday"] = df["date"].dt.weekday

    X = df[
        ["day", "month", "weekday"]
    ]

    y = df["units_sold"]

    model = XGBRegressor()

    model.fit(X, y)

    latest = X.tail(1)

    prediction = int(
        model.predict(latest)[0]
    )

    return prediction * 30