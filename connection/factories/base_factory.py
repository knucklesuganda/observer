

class BaseProtocolFactory:
    def __call__(self, *args, **kwargs):
        raise NotImplementedError("You need to return Protocol() in __call__()")
