import check
from PyQt5.QtCore import QRunnable, pyqtSlot, pyqtSignal, QObject
import time


class XHaveWTU(QRunnable):
    def __init__(self, x_file: str, WTUlist: list, to_file: str):
        super().__init__()
        self.x_file = x_file
        self.wtulist = WTUlist
        self.to_file = to_file

        self.signals = WorkerSignal()

    @pyqtSlot()
    def run(self):
        self.signals.start.emit(False)
        line_numbers = check.iter_count(self.x_file)
        self.signals.process_max.emit(line_numbers)
        #        print(line_numbers)
        counter = 0
        try:
            with open(self.x_file) as fr:
                with open(self.to_file, 'w')as tf:
                    for line in fr:
                        ln = float(line[49:59])
                        fp = float(line[59:69])
                        tp = float(line[69:79])
                        for l in self.wtulist:
                            if l[0] == ln:
                                if fp <= l[1] <= tp:
                                    tf.write(line)
                                    break
                        counter += 1

                        if counter % 100000 == 0:
                            self.signals.process.emit(counter)
                            # print(counter)
        except Exception as e:
            print(str(e))
        self.signals.process.emit(counter)
        self.signals.finished.emit(True)


class WorkerSignal(QObject):
    start = pyqtSignal(bool)
    process = pyqtSignal(int)
    process_max = pyqtSignal(int)
    finished = pyqtSignal(bool)
