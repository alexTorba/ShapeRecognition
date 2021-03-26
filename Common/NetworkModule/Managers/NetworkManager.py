from Common.JsonFormatterModule.JsonContract import JsonContract
from Common.JsonFormatterModule.JsonFormatter import JsonFormatter
from Common.NetworkModule.Handlers.MethodHandler import MethodHandler
from Common.NetworkModule.Managers.BaseNetworkManager import BaseNetworkManager


class NetworkManager:

    @staticmethod
    def send(path: str, data: JsonContract, response_type: type) -> JsonContract:
        data_json = JsonFormatter.serialize(data)
        response_json = BaseNetworkManager.send(path, data_json)
        return JsonFormatter.deserialize(response_json, response_type)

    @staticmethod
    def get(path: str, response_type: type) -> JsonContract:
        response_json = BaseNetworkManager.get(path)
        return JsonFormatter.deserialize(response_json, response_type)

    @staticmethod
    def start_listening(method_handler: MethodHandler):
        BaseNetworkManager.start_listening(method_handler)
