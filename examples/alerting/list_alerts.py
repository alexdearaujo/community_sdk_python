"""List active alerts.

Uses the alert_list operation from the AlertService group.
The POST body is required; an empty AlertServiceListRequest returns all alerts.
"""

from kentik_api.client import KentikAPI
from kentik_api.gen.alerting.models import AlertServiceListRequest


def main() -> None:
    client = KentikAPI()

    # Fetch the first page of alerts with default filters.
    response = client.alerting.alert_list(data=AlertServiceListRequest())
    alerts = [alert for alert in (response.alerts or []) if alert is not None]
    print(f"Found {len(alerts)} active alert(s).")
    for alert in alerts[:10]:
        sev = alert.severity if alert.severity else "-"
        print(f"  {alert.id}: severity={sev} state={alert.state}")


if __name__ == "__main__":
    main()
