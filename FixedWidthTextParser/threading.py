import time
from PyQt5.QtCore import QObject, QRunnable, QThreadPool, QTime, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QProgressBar, QPushButton, QVBoxLayout, QWidget


class WorkerSignal(QObject):
    progress = pyqtSignal(int)


class Worker(QRunnable):
    def __init__(self):
        super().__init__()
        self.signals = WorkerSignal()

    @pyqtSlot()
    def run(self):
        total_n = 100
        for n in range(total_n):
            progress_pc = int(100 * float(n + 1) / total_n)
            self.signals.progress.emit(progress_pc)
            time.sleep(0.01)


class Mainwindow(QMainWindow):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        layout = QVBoxLayout
        self.progress = QProgressBar
        button = QPushButton('Test')
        button.pressed.connect(self.excute)
        layout.addWidget(self.progress)


