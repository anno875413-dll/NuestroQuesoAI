import pandas as pd


def estimated_loss():

    inventory = pd.read_csv(
        "data/inventory_data.csv"
    )

    total_units = inventory[
        "quantity"
    ].sum()

    loss = total_units * 4.50

    return round(
        loss,
        2
    )