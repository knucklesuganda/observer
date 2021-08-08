from typing import Union
from uuid import UUID

from pydantic import BaseModel

from logic.data_structures.typings import IP_ADDRESS


class Observation(BaseModel):
    observer: UUID
    target: Union[UUID, None]

    observer_ip: IP_ADDRESS
    target_ip: IP_ADDRESS

    is_healthy: bool
