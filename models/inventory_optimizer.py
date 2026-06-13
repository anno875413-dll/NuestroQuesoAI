import pandas as pd


def current_inventory(cheese_type):

    inventory = pd.read_csv(
        "data/inventory_data.csv"
    )

    inventory = inventory[
        inventory["cheese_type"] == cheese_type
    ]

    return int(
        inventory["quantity"].sum()
    )