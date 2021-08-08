from asyncio import transports
from typing import Tuple, Text, Union, Iterable

from connection.protocols.base_protocol import BaseProtocol


class ObserverProtocol(BaseProtocol):
    def __init__(self, my_address, observer_addresses: Iterable):
        self.my_address = my_address
        self.observer_addresses = list(observer_addresses)

        print(f"Working on {self.my_address} address")
        print(f"Known observers: {self.observer_addresses}")

    def datagram_received(self, data: Union[bytes, Text], addr: Tuple[str, int]):
        data, addr = super(ObserverProtocol, self).datagram_received(data=data, addr=addr)

        if data['type'] == 'connection_made':
            if data['observer_address'] != self.my_address:
                self.observer_addresses.append(self.observer_addresses)
                print("New observer was added to the known list")

        print(addr, ":", data)

    def connection_made(self, transport: transports.BaseTransport) -> None:
        for observer in self.observer_addresses:
            self.data_write(
                transport=transport,
                data={
                    "type": "connection_made",
                    "my_address": self.my_address,
                    "observer_address": transport.get_extra_info('address'),
                },
                address=observer
            )
