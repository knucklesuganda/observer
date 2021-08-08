import json
import asyncio
from typing import Union, Text, Tuple, Dict

from connection.serializers.base_serializer import BaseSerializer


class BaseProtocol(asyncio.DatagramProtocol):
    def __init__(self):
        self.transport = None

    def serialize_data(self, data):
        return json.dumps({"data": data}, cls=BaseSerializer).encode("utf-8")

    def deserialize_data(self, data):
        try:
            return json.loads(data.decode('utf-8'))['data']
        except (json.JSONDecodeError, KeyError) as exc:
            raise ValueError(exc)

    def send_data(self, data, address):
        self.transport.sendto(data=self.serialize_data(data=data), addr=address)

    def datagram_received(
        self, data: Union[bytes, Text], addr: Tuple[str, int],
    ) -> Tuple[Dict, Tuple[str, int]]:
        return self.deserialize_data(data=data), addr

    def connection_made(self, transport) -> None:
        self.transport = transport
