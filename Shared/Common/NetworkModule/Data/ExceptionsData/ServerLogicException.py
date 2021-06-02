class ServerLogicException(Exception):
    state_code: int
    message: str

    def __init__(self, state_code: int, message: str):
        self.state_code = state_code
        self.message = message
