from Client.Common.EventParam import EventParam
from Client.Model.SimpleModel import SimpleModel
from Client.View.Main.MainView import MainView


class MainPresenter:
    def __init__(self, view: MainView):
        self._model = SimpleModel()
        self._view = view
        self._init_handlers()

    def _init_handlers(self):
        self._view.pushButton_signal.connect(self.pushButton_clicked_handler)

    def pushButton_clicked_handler(self, param: EventParam):
        print(f"Presenter. In pushButton_clicked_handler, sender = {param.sender}, message = {param.args.message}")
        print(f"Model logic. {self._model.get_random_value()}")
