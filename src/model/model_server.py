from src import *
import datetime
from pyModbusTCP.server import ModbusServer
from time import sleep
import logging

logging.basicConfig(filename="server.log", level=logging.DEBUG)

NOW = datetime.datetime.now().strftime('%Y/%m/%d - %H:%M:%S')


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
                self.notification.emit(f"{NOW}\tStart server {self.ip}:{self.port} ...")
                logging.info(f"{NOW}\t\tStart server {self.ip}:{self.port} ...")
                self.notification.emit(f"{NOW}\tServer is online")
                logging.info(f"{NOW}\t\tServer is online")
                while self.thread_active:
                    if not self.thread_active:
                        break
                    sleep(1)
                    self.status.emit("Server in process")
            except ConnectionError as ce:
                self.notification.emit(f"{str(ce)}")
                logging.warning(f"{NOW}\t\t{str(ce)}")
                self.stop()
            except OSError as oe:
                self.notification.emit(f"{str(oe)}")
                logging.warning(f"{NOW}\t\t{str(oe)}")
                self.stop()

    def stop(self):
        self.notification.emit(f"Shutdown server ...")
        logging.info(f"{NOW}\t\tShutdown server ...")
        self.server.stop()
        self.notification.emit(f"{NOW}\tServer is offline")
        logging.info(f"{NOW}\t\tServer is offline")
        self.thread_active = False
        self.enable_process.emit(False)
        self.quit()
