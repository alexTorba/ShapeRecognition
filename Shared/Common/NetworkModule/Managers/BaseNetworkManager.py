from http.server import HTTPServer

import requests  # pip install requests

from Shared.Common.NetworkModule.Handlers.HttpRequestHandler import HttpRequestHandler
from Shared.Common.NetworkModule.Handlers.MethodHandler import MethodHandler
from Shared.Common.NetworkModule.Managers.UrlManager import UrlManager


class BaseNetworkManager:

    @staticmethod
    def send(path: str, data: str) -> str:
        url = UrlManager.get_url(path)
        response: str = ""
        try:
            response = requests.post(url, data).content.decode("utf-8")
        except Exception as e:
            print(e)
        return response

    @staticmethod
    def get(path: str) -> str:
        url = UrlManager.get_url(path)
        response: str = ""
        try:
            response = requests.get(url).content.decode("utf-8")
        except Exception as e:
            print(f"Connection error ! {e}")
        return response

    @staticmethod
    def start_listening(method_handler: MethodHandler):
        httpd = HTTPServer(("localhost", 8000), HttpRequestHandler)
        HttpRequestHandler.method_handler = method_handler
        httpd.serve_forever()
