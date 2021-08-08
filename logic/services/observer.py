import asyncio
import uuid

from pydantic import ValidationError

import settings
from logic.data_structures.observation import Observation
from connection.factories.observer_protocol import ObserverProtocolFactory
from logic.data_structures.observation_message import ObservationMessage, MessageTypeEnum


class Observer:
    def __init__(self):
        self.protocol = None
        self.observation = None
        self.event_loop = asyncio.get_event_loop()

    async def start(self):
        try:
            self.observation = Observation(
                observer=uuid.uuid4(),
                target=None,
                observer_ip=settings.OBSERVER_ADDRESS,
                target_ip=settings.TARGET_ADDRESS,
                is_healthy=False,
            )
        except ValidationError as exc:
            print(f"Observation validation error. Exception: {exc}")
            return

        protocol_factory = ObserverProtocolFactory()
        self.protocol = await protocol_factory.create_protocol(
            observer_address=self.observation.observer_ip,
            target_address=self.observation.target_ip,
            connection_made_callback=self.connection_made,
            data_received_callback=self.data_received,
        )

        self.send_data(
            message_type=MessageTypeEnum.INITIAL_CONNECTION_PING.value,
            message_data=f"initial_connection initializer from {self.observation.observer}",
        )

    def send_data(self, message_type, message_data, address=None):
        try:
            observation_message = ObservationMessage(
                observer=self.observation.observer,
                observer_ip=self.observation.observer_ip,
                target_ip=self.observation.target_ip,
                message_type=message_type,
                message_data=message_data,
            )
        except ValidationError as exc:
            print(f"ObservationMessage validation error. Exception: {exc}")
            return

        self.protocol.send_data(
            data=observation_message.dict(),
            address=address or observation_message.target_ip,
        )

    def connection_made(self, transport):
        print("Connection was made")

    def data_received(self, data, address):
        try:
            observation_message = ObservationMessage(**data)
        except ValidationError as exc:
            print(f"Address {address} sent a message, but it was invalid. Exceptions: {exc}")
            return

        print(observation_message.dict())

        if observation_message.message_type == MessageTypeEnum.INITIAL_CONNECTION_PING.value:
            print(f"Observer {observation_message.observer} requested initial ping.")

            self.send_data(
                message_type=MessageTypeEnum.INITIAL_CONNECTION_PONG.value,
                message_data=f"initial_connection initialized with {self.observation.observer}",
            )
        elif observation_message.message_type == MessageTypeEnum.INITIAL_CONNECTION_PONG.value:
            print(f"Observer {observation_message.observer} responded to the initial ping.")

