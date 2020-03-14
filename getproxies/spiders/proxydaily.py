import requests
from parsel import Selector

from getproxies.proxy import Proxy, Protocol
from getproxies.spiders.base import Spider


class ProxyDailySpider(Spider):
    """Spider for proxy-daily.com proxy list"""
    name = 'proxy-daily.com'
    urls = ['http://www.proxy-daily.com']

    def scrape_url(self, url):
        response = requests.get(url)
        sel = Selector(text=response.text)
        boxes = sel.css('div#free-proxy-list .freeProxyStyle')
        proxies = set()
        for i, box in enumerate(boxes):
            protocol: Protocol
            if i == 0:
                protocol = 'https'
            elif i == 1:
                protocol = 'socks4'
            elif i == 2:
                protocol = 'socks5'
            else:  # unhandled boxes bye bye
                continue
            for line in box.xpath('text()').extract_first().splitlines():
                host, port = line.split(':')
                proxies.add(
                    Proxy(
                        host=host,
                        port=port,
                        protocol=protocol,
                        source=self.name,
                    )
                )
        return proxies

