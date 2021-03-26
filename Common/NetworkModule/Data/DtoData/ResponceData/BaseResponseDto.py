from Common.JsonFormatterModule.JsonContract import JsonContract


class BaseResponseDto(JsonContract):
    state_code: int
    __json_fields = {"s": "state_code"}

    def __init__(self, state_code: int = None):
        super().__init__(self.__json_fields)

        if state_code is not None:
            self.state_code = state_code
