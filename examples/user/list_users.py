"""List all users in the account."""

from kentik_api.client import KentikAPI


def main() -> None:
    client = KentikAPI()
    response = client.user.list_users()
    users = response.users or []
    print(f"Found {len(users)} user(s).")
    for user in users[:10]:
        print(f"  {user.id}: {user.userEmail} ({user.userFullName})")


if __name__ == "__main__":
    main()
