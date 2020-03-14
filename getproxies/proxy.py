from dataclasses import dataclass
from typing import Literal

Protocol = Literal['https', 'http', 'socks4', 'socks5']


@dataclass
class Proxy:
    host: str
    port: str
    protocol: Protocol
    code: str = ''
    country: str = ''
    anonymous: bool = False
    source: str = ''

    def __str__(self):
        return f'{self.protocol}://{self.host}:{self.port}'

    def __repr__(self):
        return str(self)

    def __hash__(self):
        return hash(str(self))

    def __eq__(self, other):
        return str(self) == str(other)


