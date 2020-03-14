from getproxies.spiders.freeproxylist import FreeProxyListSpider
from getproxies.spiders.proxydaily import ProxyDailySpider

SPIDERS = [FreeProxyListSpider, ProxyDailySpider]

__all__ = ['FreeProxyListSpider', 'ProxyDailySpider', 'SPIDERS']
