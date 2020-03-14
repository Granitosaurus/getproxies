from typing import Type, List

from getproxies.proxy import Protocol
from getproxies.spiders import SPIDERS
from getproxies.spiders.base import Spider


class ProxyManager:
    def __init__(
            self,
            limit: int = None,
            protocol: Protocol = None,
            country: str = None,
            spiders: List[Type[Spider]] = SPIDERS
    ):
        self.spiders = spiders
        self.limit = limit
        self.protocol = protocol
        self.country = country

    def scrape(self):
        """Scrape proxies from free proxy sources"""
        all_proxies = set()
        for spider_cls in self.spiders:
            proxies = spider_cls().scrape()
            if self.protocol:
                proxies = {p for p in proxies if p.protocol == self.protocol}
            if self.country:
                proxies = {p for p in proxies if p.country == self.country}
            all_proxies = all_proxies.union(proxies)
            if self.limit and len(list(all_proxies)) >= self.limit:
                return all_proxies
        return all_proxies


def get_proxies(limit: int = None, protocol: Protocol = None, country: str = None):
    """scrape and process proxies from all free proxy sources"""
    manager = ProxyManager(limit=limit, protocol=protocol, country=country)
    return list(manager.scrape())


if __name__ == '__main__':
    proxies = get_proxies()
    print(set([p.protocol for p in proxies]))
