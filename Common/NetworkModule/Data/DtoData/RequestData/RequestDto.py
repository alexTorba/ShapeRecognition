import typing
from typing import TypeVar

from Common.JsonFormatterModule.JsonContract import JsonContract
from Common.NetworkModule.Data.DtoData.RequestData.BaseRequestDto import BaseRequestDto

T = TypeVar("T", bound=JsonContract)


class RequestDto(BaseRequestDto, typing.Generic[T]):
    data: T
    __json_field = {"d": "data"}

    def __init__(self, server_method: str = None, data: T = None):
        super().__init__(server_method)

        if data is not None:
            self.data = data
        self._update_json_fields(self.__json_field)
