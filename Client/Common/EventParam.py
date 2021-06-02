from Client.Common.EventArgs import EventArgs


class EventParam:
    def __init__(self, sender: object, args: EventArgs = EventArgs()):
        self.sender = sender
        self.args = args
