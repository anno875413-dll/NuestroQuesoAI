from models.production_planner import (
    production_needed
)


def daily_report():

    return {

        "Queso Fresco":
            production_needed(
                "Queso Fresco"
            ),

        "Queso Oaxaca":
            production_needed(
                "Queso Oaxaca"
            )
    }