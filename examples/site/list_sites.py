"""List sites and site markets in the account."""

from kentik_api.client import KentikAPI


def main() -> None:
    client = KentikAPI()

    sites_resp = client.site.list_sites()
    sites = sites_resp.sites or []
    print(f"Found {len(sites)} site(s).")
    for site in sites[:5]:
        print(f"  {site.id}: {site.title}")

    markets_resp = client.site.list_site_markets()
    markets = markets_resp.siteMarkets or []
    print(f"\nFound {len(markets)} site market(s).")
    for market in markets[:5]:
        print(f"  {market.id}: {market.name}")


if __name__ == "__main__":
    main()
