from src import *
from src.view.ui_main_window import Ui_MainWindow
from src.model.model_server import ServerWorker


class MainWindow(qtw.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(qtc.Qt.WindowCloseButtonHint | qtc.Qt.WindowMinimizeButtonHint)
        self.modbus_server = None
        self.reg_ip_validator()
        self.btn_start.clicked.connect(self.start_server)
        self.btn_stop.clicked.connect(self.stop_server)
        self.enable_disable_objects(val=False)
        self.show()

    def reg_ip_validator(self):
        ip_range = "^(([1-9][0-9]?|1[0-9]{2}|2[0-4][0-9]|25[0-4])\.([0-9][0-9]?|1[0-9]{2}|2[0-4][0-9]|25[0-4])\." \
                   "([0-9][0-9]?|1[0-9]{2}|2[0-4][0-9]|25[0-4])\.([0-9][0-9]?|1[0-9]{2}|2[0-4][0-9]|25[0-4])$)"
        ip_regex = qtc.QRegExp(ip_range)
        ip_validator = qtg.QRegExpValidator(ip_regex)
        self.le_ip.setValidator(ip_validator)

    def start_server(self):
        ip = self.le_ip.text()
        port = self.sb_port.value()
        if len(ip) <= 7 or ip[-1:] == ".":
            self.message_notification("Check your IP address!")
        else:
            self.modbus_server = ServerWorker(ip=ip, port=port)
            self.modbus_server.start()
            self.modbus_server.enable_process.connect(self.enable_disable_objects)
            self.modbus_server.notification.connect(self.message_notification)
            self.modbus_server.status.connect(self.message_status_bar)

    def stop_server(self):
        self.modbus_server.stop()

    def message_notification(self, msg):
        self.lw_notification.addItem(msg)
        self.lw_notification.scrollToBottom()

    def message_status_bar(self, msg):
        self.statusbar.showMessage(msg)

    def enable_disable_objects(self, val):
        if val:
            self.le_ip.setEnabled(False)
            self.sb_port.setEnabled(False)
            self.btn_start.setEnabled(False)
            self.btn_stop.setEnabled(True)

        else:
            self.le_ip.setEnabled(True)
            self.sb_port.setEnabled(True)
            self.btn_start.setEnabled(True)
            self.btn_stop.setEnabled(False)

    def keyPressEvent(self, e):
        if e.key() == qtc.Qt.Key_Enter or e.key() == qtc.Qt.Key_Return:
            if not isinstance(self.modbus_server, ServerWorker):
                self.start_server()
            else:
                if self.modbus_server.isFinished():
                    self.start_server()
        elif e.key() == qtc.Qt.Key_Escape:
            if isinstance(self.modbus_server, ServerWorker):
                if self.modbus_server.isRunning():
                    self.stop_server()

    def closeEvent(self, e):
        if isinstance(self.modbus_server, ServerWorker):
            if self.modbus_server.isRunning():
                self.modbus_server.stop()
            e.accept()
        else:
            e.accept()
