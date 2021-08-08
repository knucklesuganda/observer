import asyncio

import settings
from connection.factories.observer_protocol import ObserverProtocolFactory


async def main():
    protocol_factory = ObserverProtocolFactory()

    await loop.create_datagram_endpoint(
        lambda: protocol_factory(),
        local_addr=settings.MY_ADDRESS,
        remote_addr=settings.INITIAL_OBSERVER,
        allow_broadcast=True,
    )


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.run_forever()
