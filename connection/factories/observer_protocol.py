import settings
from connection.factories.base_factory import BaseProtocolFactory
from connection.protocols.observer_protocol import ObserverProtocol


class ObserverProtocolFactory(BaseProtocolFactory):
    def __call__(self, *args, **kwargs):
        return ObserverProtocol(
            my_address=settings.MY_ADDRESS,
            observer_addresses=[
                settings.INITIAL_OBSERVER
            ],
        )
