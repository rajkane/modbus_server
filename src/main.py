import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication
from src.controller.main_window import MainWindow


def run():
    app = QApplication(sys.argv)
    app.setApplicationName("Modbus Server")
    app.setWindowIcon(QIcon("server.ico"))
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    run()
