from Shared.Common.JsonFormatterModule.JsonContract import JsonContract


class UrlInfo(JsonContract):
    ip_address: str
    port: int

    __json_fields = {
        "i": "ip_address",
        "p": "port"
    }

    def __init__(self, ip_address: str = None, port: int = None):
        super().__init__(self.__json_fields)

        if ip_address is not None:
            self.ip_address = ip_address
        if port is not None:
            self.port = port

    def __repr__(self) -> str:
        return f"{self.ip_address}:{self.port}"
