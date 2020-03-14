import click

from getproxies import get_proxies


@click.command()
@click.option('-p', '--protocol', help='restrict to specific protocol', type=click.Choice(['https', 'http', 'socks4', 'socks5']))
@click.option('-c', '--country', help='only proxies from specified country (ISO double char code, e.g. US)')
@click.option('-l', '--limit', help='limit proxy retrieval - increases performance', type=click.INT)
@click.option('-f', '--format',
              help='proxy output format, available variables: host,port,protocol,code,country,anonymous,source',
              default='{protocol}://{host}:{port}', show_default=True)
def main(protocol, country, limit, format):
    """scrape free proxies from all sources and put it to STDOUT"""
    proxies = get_proxies(limit=limit, protocol=protocol, country=country)
    for proxy in proxies:
        click.echo(format.format(**proxy.__dict__))


if __name__ == '__main__':
    main()
