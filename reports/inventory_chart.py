import pandas as pd
import plotly.express as px


def create_inventory_chart():

    inventory = pd.read_csv(
        "data/inventory_data.csv"
    )

    grouped = inventory.groupby(
        "cheese_type"
    )["quantity"].sum().reset_index()

    fig = px.bar(
        grouped,
        x="cheese_type",
        y="quantity",
        title="Current Inventory"
    )

    return fig