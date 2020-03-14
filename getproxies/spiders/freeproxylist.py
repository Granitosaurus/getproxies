import requests
from parsel import Selector

from getproxies.proxy import Proxy, Protocol
from getproxies.spiders.base import Spider


class FreeProxyListSpider(Spider):
    name = 'free-proxy-list.net'
    urls = [
        # these are all the same layout but different domain names
        'http://www.free-proxy-list.net',
        'https://free-proxy-list.net/anonymous-proxy.html',
        'https://www.us-proxy.org/',
        'https://free-proxy-list.net/uk-proxy.html',
        'https://www.sslproxies.org/',
    ]

    def scrape_url(self, url):
        response = requests.get(url)
        sel = Selector(text=response.text)
        table = sel.css('table#proxylisttable')
        proxies = set()

        for row in table.xpath('tbody/tr'):
            data = row.xpath('.//td/text()').extract()
            protocol: Protocol = 'https' if data[6].lower() == 'yes' else 'http'
            try:
                proxies.add(
                    Proxy(
                        host=data[0],
                        port=data[1],
                        protocol=protocol,
                        code=data[2].lower(),
                        country=data[3].lower(),
                        anonymous=data[4].lower() in ('anonymous', 'elite proxy'),
                        source=self.name,
                    )
                )
            except Exception as e:
                self.log.warning(f'failed to parse proxy from {data} got {e}')
        return proxies


