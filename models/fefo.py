import pandas as pd


def fefo_inventory():

    inventory = pd.read_csv(
        "data/inventory_data.csv"
    )

    inventory = inventory.sort_values(
        "expiration_date"
    )

    return inventory