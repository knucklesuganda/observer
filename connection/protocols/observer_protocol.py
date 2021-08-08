from asyncio import transports

from connection.protocols.base_protocol import BaseProtocol
from logic.data_structures.typings import IP_ADDRESS


class ObserverProtocol(BaseProtocol):
    def __init__(
        self,
        connection_made_callback: callable,
        data_received_callback: callable,
        observer_address: IP_ADDRESS,
        target_address: IP_ADDRESS,
    ):
        super(ObserverProtocol, self).__init__()
        self.connection_made_callback = connection_made_callback
        self.data_received_callback = data_received_callback

        self.observer_address = observer_address
        self.target_address = target_address

    def connection_made(self, transport: transports.BaseTransport) -> None:
        super(ObserverProtocol, self).connection_made(transport=transport)
        return self.connection_made_callback(transport=transport)

    def datagram_received(self, data, addr):
        data, addr = super(ObserverProtocol, self).datagram_received(data=data, addr=addr)
        return self.data_received_callback(data=data, address=addr)
