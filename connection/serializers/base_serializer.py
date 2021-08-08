import json
from enum import Enum
from uuid import UUID


class BaseSerializer(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, (UUID, Enum)):
            return str(o)
        else:
            return super(BaseSerializer, self).default(o)
