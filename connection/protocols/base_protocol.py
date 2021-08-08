import json
import asyncio
from typing import Union, Text, Tuple, Dict


class BaseProtocol(asyncio.DatagramProtocol):
    def serialize_data(self, data):
        return json.dumps({"data": data}).encode("utf-8")

    def deserialize_data(self, data):
        try:
            return json.loads(data.decode('utf-8'))['data']
        except (json.JSONDecodeError, KeyError) as exc:
            raise ValueError(exc)

    def data_write(self, transport, data, address):
        transport.sendto(self.serialize_data(data=data), addr=address)

    def datagram_received(
        self, data: Union[bytes, Text], addr: Tuple[str, int],
    ) -> Tuple[Dict, Tuple[str, int]]:
        return self.deserialize_data(data=data), addr
