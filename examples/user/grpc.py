# HAND-WRITTEN: not modified by `make generate`. Edit directly.
"""List all users in the account — gRPC transport."""

from kentik_api.client import KentikAPI
from kentik_api.errors import KentikError


def main() -> None:
    client = KentikAPI(protocol="grpc")
    try:
        response = client.user.list_users()
        users = [user for user in (response.users or []) if user is not None]
        print(f"Found {len(users)} user(s).")
        for user in users[:10]:
            print(f"  {user.id}: {user.userEmail} ({user.userFullName})")
    except KentikError as exc:
        print(f"API error over gRPC: {exc}")


if __name__ == "__main__":
    main()
