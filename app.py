from fastapi import FastAPI

from models.demand_forecast import (
    forecast_cheese_demand
)

app = FastAPI()


@app.get("/")
def home():

    return {
        "message":
        "Nuestro Queso AI Running"
    }


@app.get("/forecast")
def forecast():

    return {

        "Queso Fresco":
            forecast_cheese_demand(
                "Queso Fresco"
            ),

        "Queso Oaxaca":
            forecast_cheese_demand(
                "Queso Oaxaca"
            )
    }