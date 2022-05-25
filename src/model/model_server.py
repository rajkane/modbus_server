from src import *
import datetime

from pyModbusTCP.server import ModbusServer, DataBank
from time import sleep
from random import uniform


class ServerWorker(qtc.QThread):
    enable_process = qtc.pyqtSignal(bool)
    state = qtc.pyqtSignal(list)
    notification = qtc.pyqtSignal(str)
    status = qtc.pyqtSignal(str)

    def __init__(self, ip: str, port: int):
        super(ServerWorker, self).__init__()
        self.thread_active = None
        self.ip = ip
        self.port = port
        self.server = None

    def run(self):
        self.thread_active = True
        self.enable_process.emit(True)
        try:
            if self.ip != "":
                self.server = ModbusServer(self.ip, self.port, no_block=True)
                self.notification.emit(f"{datetime.datetime.now()} Start server ...")
                self.status.emit(f"{datetime.datetime.now()} Start server ...")
                self.server.start()
                self.notification.emit("Server is online")
                state = [0]
                while self.thread_active:
                    DataBank.set_words(0, [int(uniform(0, 100))])
                    if state != DataBank.get_words(1):
                        state = DataBank.get_words(1)
                        self.notification.emit(f"Value of register 1 has changed to {str(state)}")
                    sleep(1)
                    self.status.emit("Server in process")
            else:
                self.stop()
                self.notification.emit("Enter ip address!")
        except ConnectionError as ce:
            self.notification.emit("Shutdown server ...")
            self.server.stop()
            self.notification.emit(f"Server is offline, {str(ce)}")
        except OSError as oe:
            self.notification.emit("Shutdown server ...")
            self.server.stop()
            self.notification.emit(f"Server is offline, {str(oe)}")

    def stop(self):
        self.notification.emit("Server is offline")
        self.thread_active = False
        self.enable_process.emit(False)
        self.status.emit("Server is offline")
        self.quit()
