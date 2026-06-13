import pandas as pd
import plotly.express as px


def create_sales_chart():

    df = pd.read_csv(
        "data/historical_sales.csv"
    )

    fig = px.line(
        df,
        x="date",
        y="units_sold",
        color="cheese_type",
        title="Historical Cheese Sales"
    )

    return fig