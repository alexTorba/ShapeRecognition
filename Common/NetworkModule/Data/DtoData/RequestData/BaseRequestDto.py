from Common.JsonFormatterModule.JsonContract import JsonContract


class BaseRequestDto(JsonContract):
    server_method: str
    client_ip: str
    client_port: int

    __json_fields = {
        "s": "server_method",
        "i": "client_ip",
        "p": "client_port"
    }

    def __init__(self, server_method: str = None, client_ip: str = None, client_port: int = None):
        super().__init__(self.__json_fields)

        if server_method is not None:
            self.server_method = server_method
        if client_ip is not None:
            self.client_ip = client_ip
        if client_port is not None:
            self.client_port = client_port
