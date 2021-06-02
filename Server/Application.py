from Shared.Common.NetworkModule.Handlers.MethodHandler import MethodHandler
from Shared.Common.NetworkModule.Managers.NetworkManager import NetworkManager


# noinspection PyAttributeOutsideInit
class Application:
    def configure(self) -> "Application":
        method_by_name = {
            # todo: add method handlers
        }
        self.method_handler = MethodHandler(method_by_name)
        return self

    def start(self):
        if not hasattr(self, "method_handler"):
            raise Exception("Server not configured!")

        print("Server Start listening..")
        NetworkManager.start_listening(method_handler=self.method_handler)
