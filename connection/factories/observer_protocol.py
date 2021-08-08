import asyncio

from connection.factories.base_factory import BaseProtocolFactory
from connection.protocols.observer_protocol import ObserverProtocol
from logic.data_structures.typings import IP_ADDRESS


class ObserverProtocolFactory(BaseProtocolFactory):
    async def create_protocol(
        self,
        observer_address: IP_ADDRESS,
        target_address: IP_ADDRESS,
        connection_made_callback: callable,
        data_received_callback: callable,
    ):
        transport, protocol = await asyncio.get_event_loop().create_datagram_endpoint(
            lambda: ObserverProtocol(
                connection_made_callback=connection_made_callback,
                data_received_callback=data_received_callback,
                observer_address=observer_address,
                target_address=target_address,
            ),
            local_addr=observer_address,
            remote_addr=target_address,
            allow_broadcast=True,
        )
        return protocol
