from alerts.alert_engine import (
    generate_alerts
)


def email_message():

    alerts = generate_alerts()

    body = "\n".join(alerts)

    return body