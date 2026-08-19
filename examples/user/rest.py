"""List all users in the account."""

from kentik_api.client import KentikAPI


def main() -> None:
    client = KentikAPI(protocol="rest")
    response = client.user.list_users()
    users = [user for user in (response.users or []) if user is not None]
    print(f"Found {len(users)} user(s).")
    for user in users[:10]:
        print(f"  {user.id}: {user.userEmail} ({user.userFullName})")


if __name__ == "__main__":
    main()
