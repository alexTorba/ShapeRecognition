from Client.Presenter.Main.MainPresenter import MainPresenter
from Client.View.Main.MainView import MainView
from Client.View.Main.ui_main_window import Ui_MainWindow


class Application:
    def __init__(self):
        self._view = MainView(Ui_MainWindow())
        self._presenter = MainPresenter(self._view)

    def start(self):
        self._view.start()
