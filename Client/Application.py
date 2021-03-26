from PyQt5 import QtWidgets
import sys

from Client.ui_main_window import Ui_MainWindow


class Application:
    def start(self):
        app = QtWidgets.QApplication(sys.argv)
        window = QtWidgets.QMainWindow()

        ui = Ui_MainWindow()
        ui.setupUi(window)

        window.show()
        sys.exit(app.exec())
