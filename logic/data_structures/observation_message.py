from enum import Enum
from uuid import UUID
from typing import Dict, Text, Union

from pydantic import BaseModel, validator

from logic.data_structures.typings import IP_ADDRESS


class MessageTypeEnum(Enum):
    INITIAL_CONNECTION_PING = "initial_connection_ping"
    INITIAL_CONNECTION_PONG = "initial_connection_pong"
    HEALTH_CHECK = "health_check"


class ObservationMessage(BaseModel):
    observer: UUID
    observer_ip: IP_ADDRESS
    target_ip: IP_ADDRESS

    message_type: Text
    message_data: Union[Dict, Text]

    @validator('message_type')
    def validate_message_type_in_enum(cls, value):
        if value not in map(lambda enum_entry: enum_entry.value, MessageTypeEnum):
            raise ValueError("message_type is invalid")
        return value
