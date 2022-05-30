from src import *
import datetime
from pyModbusTCP.server import ModbusServer
from time import sleep
import logging

logging.basicConfig(filename="server.log", filemode="w", level=logging.DEBUG,
                    format="%(asctime)s\t\t%(levelname)s: %(message)s", datefmt='%Y/%m/%d %H:%M:%S')


def date_time_now():
    return datetime.datetime.now().strftime('%Y/%m/%d - %H:%M:%S')


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
                self.notification.emit(f"{date_time_now()}\tStart server {self.ip}:{self.port} ...")
                logging.info(f"Start server {self.ip}:{self.port} ...")
                self.notification.emit(f"{date_time_now()}\tServer is online")
                logging.info(f"Server is online")
                while self.thread_active:
                    if not self.thread_active:
                        break
                    sleep(1)
                    self.status.emit("Server in process")
            except ConnectionError as ce:
                self.notification.emit(f"{str(ce)}")
                logging.warning(f"{self.ip}:{self.port} {str(ce)}")
                self.stop()
            except OSError as oe:
                self.notification.emit(f"{str(oe)}")
                logging.warning(f"{self.ip}:{self.port} {str(oe)}")
                self.stop()

    def stop(self):
        self.notification.emit(f"Shutdown server ...")
        logging.info(f"Shutdown server ...")
        self.server.stop()
        self.notification.emit(f"{date_time_now()}\tServer is offline")
        logging.info(f"Server is offline")
        self.thread_active = False
        self.enable_process.emit(False)
        self.quit()
