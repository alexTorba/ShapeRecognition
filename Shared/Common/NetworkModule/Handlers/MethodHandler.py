from typing import Union, Callable, Dict, Tuple

from Shared.Common.JsonFormatterModule.JsonFormatter import JsonFormatter
from Shared.Common.NetworkModule.Data.DtoData.RequestData.BaseRequestDto import BaseRequestDto
from Shared.Common.NetworkModule.Data.DtoData.ResponceData.BaseResponseDto import BaseResponseDto
from Shared.Common.NetworkModule.Data.ExceptionsData.ServerLogicException import ServerLogicException


class MethodHandler:
    __method_handler: Dict[str, Union[Callable[[], BaseResponseDto], Callable[[BaseRequestDto], BaseResponseDto]]]

    def __init__(self, method_handler: dict):
        self.__method_handler = method_handler

    def do_get(self, server_method: str) -> str:
        handler = self.__method_handler.get(server_method, None)
        if handler is None:
            raise ServerLogicException(400, f"Unsupported server method {server_method}!")

        response_dto = handler()
        return JsonFormatter.serialize(response_dto)

    # noinspection PyUnresolvedReferences
    def do_post(self, server_method: str, json_request_dto: str, client_address: Tuple[str, int]) -> str:
        handler = self.__method_handler.get(server_method)
        if handler is None:
            raise ServerLogicException(400, f"Unsupported server method {server_method}!")

        dto_type = handler.__annotations__["dto"]
        request_dto = JsonFormatter.deserialize(json_request_dto, dto_type)
        if not hasattr(request_dto, "data"):
            raise ServerLogicException(400, f"Server work only with dto types ! Stop spam !")

        UrlManager.resolve_client_address(request_dto, client_address)
        response_dto = handler(request_dto)
        return JsonFormatter.serialize(response_dto)

    @staticmethod
    def get_server_method_name(request_path: str) -> str:
        return request_path[1:]
