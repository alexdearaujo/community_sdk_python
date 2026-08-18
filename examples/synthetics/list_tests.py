"""List synthetic tests and agents."""

from kentik_api.client import KentikAPI


def main() -> None:
    client = KentikAPI()

    tests_resp = client.synthetics.list_tests()
    tests = tests_resp.tests or []
    print(f"Found {len(tests)} synthetic test(s).")
    for test in tests[:5]:
        print(f"  {test.id}: {test.name} (status={test.status})")

    agents_resp = client.synthetics.list_agents()
    agents = agents_resp.agents or []
    print(f"\nFound {len(agents)} synthetic agent(s).")
    for agent in agents[:5]:
        print(f"  {agent.id}: {agent.alias} ({agent.city}, {agent.country})")


if __name__ == "__main__":
    main()
