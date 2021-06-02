import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QObject

from Client.Common.EventArgs import EventArgs
from Client.Common.EventParam import EventParam
from Client.View.Main.ui_main_window import Ui_MainWindow


class MainView(QObject):
    pushButton_signal = QtCore.pyqtSignal(EventParam)

    def __init__(self, ui: Ui_MainWindow):
        super().__init__()
        self._app = QtWidgets.QApplication(sys.argv)
        self._window = QtWidgets.QMainWindow()
        self._ui = ui
        self._ui.setupUi(self._window)

        self._init_handlers()

    def _init_handlers(self):
        self._ui.pushButton.clicked.connect(self._pushButton_clicked)

    def _pushButton_clicked(self):
        print("view pushButton logic")
        self.pushButton_signal.emit(EventParam(self._ui.pushButton, EventArgs("Push!")))

    def start(self):
        self._window.show()
        sys.exit(self._app.exec())
