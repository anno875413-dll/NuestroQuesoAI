def estimated_savings(
        spoiled_units,
        cost_per_unit):

    return round(
        spoiled_units
        * cost_per_unit,
        2
    )