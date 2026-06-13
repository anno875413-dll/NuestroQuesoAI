from models.xgboost_forecast import (
    xgboost_forecast
)

from models.inventory_optimizer import (
    current_inventory
)


def production_needed(
        cheese_type):

    demand = xgboost_forecast(
        cheese_type
    )

    inventory = current_inventory(
        cheese_type
    )

    amount = max(
        0,
        demand - inventory
    )

    return amount