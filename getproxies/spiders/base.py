import logging


class Spider:
    """Base spider class for proxy spiders"""
    name = NotImplemented
    urls = NotImplemented

    def __init__(self):
        self.log = logging.getLogger(type(self).__name__)
        self.log.setLevel(logging.DEBUG)

    def scrape(self):
        proxies = set()
        for url in self.urls:
            found = self.scrape_url(url)
            proxies = proxies.union(found)
        return proxies

    def scrape_url(self, url):
        raise NotImplementedError
