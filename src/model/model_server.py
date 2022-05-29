
from src import *
import datetime

from pyModbusTCP.server import ModbusServer
from time import sleep


class ServerWorker(qtc.QThread):
    enable_process = qtc.pyqtSignal(bool)
    notification = qtc.pyqtSignal(str)
    status = qtc.pyqtSignal(str)

    def __init__(self, ip: str, port: int):
        super(ServerWorker, self).__init__()
        self.ip = ip
        self.port = port
        self.thread_active = False
        self.server = None

    def run(self):
        self.thread_active = True
        self.enable_process.emit(True)

        if self.thread_active:
            try:
                self.server = ModbusServer(self.ip, self.port, no_block=True)
                self.server.start()
                self.notification.emit("Start server ...")
                self.notification.emit(f"{datetime.datetime.now().strftime('%Y/%m/%d - %H:%M:%S')}\tServer is online")
                while self.thread_active:
                    if not self.thread_active:
                        break
                    self.status.emit("Server in process")
            except ConnectionError as ce:
                self.notification.emit(f"{str(ce)}")
                self.stop()
            except OSError as oe:
                self.notification.emit(f"{str(oe)}")
                self.stop()

    def stop(self):
        self.notification.emit("Shutdown server ...")
        self.server.stop()
        self.notification.emit(f"{datetime.datetime.now().strftime('%Y/%m/%d - %H:%M:%S')}\tServer is offline")
        self.thread_active = False
        self.enable_process.emit(False)
        self.quit()
