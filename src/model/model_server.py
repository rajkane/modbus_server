from src import *


class ServerWorker(qtc.QThread):
    def __init__(self):
        super(ServerWorker, self).__init__()
        pass

    def run(self):
        pass

    def stop(self):
        self.exit()
