from models.spoilage_prediction import (
    find_high_risk_batches
)


def waste_actions():

    high_risk = find_high_risk_batches()

    actions = []

    for _, row in high_risk.iterrows():

        actions.append(

            f"""
PROMOTE {row['cheese_type']}
Batch {row['batch_id']}
Quantity {row['quantity']}
"""
        )

    return actions