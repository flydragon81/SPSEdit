from mainwindow import Ui_MainWindow
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow
import content
import filefunction
import config
from xhaveWTU import XHaveWTU
from PyQt5.QtCore import QThreadPool
import logging
from importlib import reload


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.threadpool = QThreadPool()
        print('maximum %d thread' % self.threadpool.maxThreadCount())

        self.ui.pushButton.clicked.connect(self.open_file)
        self.ui.pushButton_2.clicked.connect(self.open_file_1)
        self.ui.pushButton_3.clicked.connect(self.process)
        self.ui.pushButton_4.clicked.connect(QtCore.QCoreApplication.instance().quit)

        self.from_file = None
        self.from_file_2 = None
        self.to_file = None
        self.ui.textEdit_3.setText('0')
        self.ui.textEdit_4.setText('5000')
        self.ui.progressBar.setValue(0)
        for i in content.content_dict.keys():
            self.ui.comboBox.addItem(str(i))
        self.list = []

    def open_file(self):
        """
            Opens WTU R file
        """
        from_file = self.from_file
        self.from_file = filefunction.file_open(self, from_file, config.r_file_pattern)
        self.ui.textEdit.setText(self.from_file)

        with open(self.from_file) as fr:
            for line in fr:
                ls = [float(line[1:11]), float(line[11:21])]
                self.list.append(ls)

    def open_file_1(self):
        """
            Opens X file
        """
        from_file_2 = self.from_file_2
        self.from_file_2 = filefunction.file_open(self, from_file_2, config.x_file_pattern)
        self.ui.textEdit_2.setText(self.from_file_2)

        self.to_file = self.from_file_2 + '.output'
        self.__prepare_logging()

    def process(self):
        worker = XHaveWTU(self.from_file_2, self.list, self.to_file)
        self.threadpool.start(worker)
        worker.signals.start.connect(self.btn_disable)
        worker.signals.process_max.connect(self.progress_max)
        worker.signals.process.connect(self.progress)
        worker.signals.finished.connect(self.btn_disable)

    def progress_max(self, file_line):
        self.ui.progressBar.setMaximum(file_line)
        self.__log(str(file_line))

    def progress(self, counter):
        self.ui.progressBar.setValue(counter)
        self.__log(str(counter))

    def btn_disable(self, statu: bool):
        self.ui.pushButton.setEnabled(statu)
        self.ui.pushButton_2.setEnabled(statu)
        self.ui.pushButton_3.setEnabled(statu)
        self.ui.pushButton_4.setEnabled(statu)

    def __prepare_logging(self):
        logging.shutdown()
        reload(logging)
        log_filename = self.from_file_2 + '.log'
        log_format = '%(asctime)s - %(threadName)s - %(levelname)s - %(message)s'
        logging.basicConfig(filename=log_filename, filemode='w', format=log_format, level=logging.NOTSET)
        logging.getLogger('sqlalchemy').setLevel(logging.ERROR)

    def __log(self, msg: str):
        logging.info(msg)
