from src import *
from src.view.ui_main_window import Ui_MainWindow


class MainWindow(qtw.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(qtc.Qt.WindowCloseButtonHint | qtc.Qt.WindowMinimizeButtonHint)
        self.reg_ip_validator()
        self.reg_port_validator()
        self.btn_start.clicked.connect(self.start_server)
        self.btn_stop.clicked.connect(self.stop_server)
        self.show()

    def reg_ip_validator(self):
        ip_range = "^(([1-9][0-9]?|1[0-9]{2}|2[0-4][0-9]|25[0-4])\.([0-9][0-9]?|1[0-9]{2}|2[0-4][0-9]|25[0-4])\." \
                   "([0-9][0-9]?|1[0-9]{2}|2[0-4][0-9]|25[0-4])\.([0-9][0-9]?|1[0-9]{2}|2[0-4][0-9]|25[0-4])$)"
        ip_regex = qtc.QRegExp(ip_range)
        ip_validator = qtg.QRegExpValidator(ip_regex)
        self.le_ip.setValidator(ip_validator)

    def reg_port_validator(self):
        port_range = "^[1-9][0-9]{4}"
        port_regex = qtc.QRegExp(f"{port_range}")
        port_validator = qtg.QRegExpValidator(port_regex)
        self.le_port.setValidator(port_validator)

    def start_server(self):
        self.lw_notification.addItem("Start server")

    def stop_server(self):
        self.lw_notification.addItem("Stop server")
