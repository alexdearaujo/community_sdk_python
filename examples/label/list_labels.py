"""List all device labels in the account."""

from kentik_api.client import KentikAPI


def main() -> None:
    client = KentikAPI()
    response = client.label.list_labels()
    labels = response.labels or []
    print(f"Found {len(labels)} label(s).")
    for label in labels:
        print(f"  {label.id}: {label.name} (color: {label.color})")


if __name__ == "__main__":
    main()
