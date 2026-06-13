import pandas as pd


def find_high_risk_batches():

    inventory = pd.read_csv(
        "data/inventory_data.csv"
    )

    today = pd.Timestamp.today()

    inventory["days_remaining"] = (
        pd.to_datetime(
            inventory["expiration_date"]
        )
        - today
    ).dt.days

    high_risk = inventory[
        inventory["days_remaining"] < 7
    ]

    return high_risk