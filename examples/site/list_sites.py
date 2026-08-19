"""List sites and site markets in the account."""

from kentik_api.client import KentikAPI


def main() -> None:
    client = KentikAPI(protocol="rest")

    sites_resp = client.site.list_sites()
    sites = [site for site in (sites_resp.sites or []) if site is not None]
    print(f"Found {len(sites)} site(s).")
    for site in sites[:5]:
        print(f"  {site.id}: {site.title}")

    markets_resp = client.site.list_site_markets()
    markets = [market for market in (markets_resp.siteMarkets or []) if market is not None]
    print(f"\nFound {len(markets)} site market(s).")
    for market in markets[:5]:
        print(f"  {market.id}: {market.name}")


if __name__ == "__main__":
    main()
