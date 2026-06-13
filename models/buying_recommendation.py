def calculate_purchase_amount(
        forecast_demand,
        current_inventory,
        safety_stock):

    purchase = (
        forecast_demand
        + safety_stock
        - current_inventory
    )

    return max(0, purchase)