import os
from typing import Tuple, Optional

from Shared.Common.JsonFormatterModule.JsonFormatter import JsonFormatter
from Shared.Common.NetworkModule.Data.DtoData.RequestData.BaseRequestDto import BaseRequestDto
from Shared.Common.NetworkModule.Data.UrlData.UrlInfo import UrlInfo


class UrlManager:
    __host: str = "127.0.0.1:8000"
    __file_name: str = "urlinfo.txt"

    @classmethod
    def get_url(cls, path: str) -> str:
        return f"http://{cls.__host}/{path}"

    @classmethod
    def set_host(cls, host: str) -> None:
        cls.__host = host

    @staticmethod
    def resolve_client_address(dto: BaseRequestDto, client_address: Tuple[str, int]):
        dto.client_ip = client_address[0]
        dto.client_port = client_address[1]

    @classmethod
    def init_url(cls):
        url_config: UrlInfo = cls.__read_from_config()
        if url_config is not None:
            cls.__host = url_config.__repr__()

    @classmethod
    def __read_from_config(cls) -> Optional[UrlInfo]:
        if os.path.exists(cls.__file_name):
            with open(cls.__file_name) as file:
                json = file.read()
                if len(json) > 0:
                    return JsonFormatter.deserialize(json, UrlInfo)
        return None
