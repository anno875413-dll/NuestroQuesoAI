def estimated_profit(
        revenue,
        production_cost,
        spoilage_loss):

    profit = (
        revenue
        - production_cost
        - spoilage_loss
    )

    return round(
        profit,
        2
    )