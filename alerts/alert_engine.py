from models.spoilage_prediction import (
    find_high_risk_batches
)


def generate_alerts():

    high_risk = find_high_risk_batches()

    alerts = []

    for _, row in high_risk.iterrows():

        alerts.append(
            f"""
Batch {row['batch_id']}
{row['cheese_type']}
Expires {row['expiration_date']}
Quantity {row['quantity']}
"""
        )

    return alerts