def temperature_risk(
        storage_temperature):

    if storage_temperature > 40:

        return "HIGH"

    elif storage_temperature > 37:

        return "MEDIUM"

    else:

        return "LOW"