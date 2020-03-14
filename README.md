# getproxies

Get some free proxies scraped from free proxy sources.

```python
from getproxies import get_proxies

proxies = get_proxies()
print(proxies[:10])
# [http://196.18.215.153:3128, https://36.67.89.179:65205, http://35.247.192.53:3128, socks5://113.54.158.40:1080, https://180.122.51.154:9999, socks4://117.44.28.152:9201, https://178.20.137.178:43980, https://109.86.121.118:46333, https://148.77.34.194:39175, socks4://114.99.16.195:1080]
```

## Sources

Currently these sources are supported 

|source|spider|
|---|---|
|[http://free-proxy-list.net](http://free-proxy-list.net)|[FreeProxyListSpider](./getproxies/spiders/freeproxylist.py)|
|[http://proxy-daily.com](http://proxy-daily.com)|[ProxyDailySpider](./getproxies/spiders/proxydaily.py)|

## extended usage

For more detailed proxy query a `ProxyManager` can be used:

```python
from getproxies import ProxyManager

proxies = ProxyManager(
    limit=10,  # only 10 proxies
    protocol='socks5',  # only socks5 proxies
    country='us',  # only us proxies
)
```

_limit parameter can reduce retrieval time_

`Proxy` objects also have extended attributes:

```python
class Proxy:
    host: str
    port: str
    protocol: str
    code: str = ''
    country: str = ''
    anonymous: bool = False
    source: str = ''
```

as strings they resolve to `protocol://host:port` template.

