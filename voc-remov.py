import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from PyQt5.QtGui import QPixmap
import traceback
from converter import make_spectro
from split_audio import fracture


class Mywidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('voc-rem.ui', self)
        self.fname = ''
        pixmap = QPixmap('./done3.png')
        self.label.setPixmap(pixmap)
        self.splt.clicked.connect(self.splitter)
        self.voc_rem.clicked.connect(self.rem_voc)
        self.spectr.clicked.connect(self.make_spectro)

    def splitter(self):
        self.fname = QFileDialog.getOpenFileName(self, 'Choose file', '', 'Sounds (*.wav)')[0]
        try:
            if self.fname != '':
                fracture(self.fname)
                print('Spectrogram has been successfully created!')
        except Exception as expr:
            raise expr

    def rem_voc(self):
        not_ready('Sorry, work in progress :((')

    def make_spectro(self):
        self.fname = QFileDialog.getOpenFileName(self, 'Choose file', '', 'Sounds (*.wav)')[0]
        try:
            if self.fname != '':
                make_spectro(self.fname)
                print('Spectrogram has been successfully created!')
        except Exception as expr:
            raise expr


def excepthook(exc_type, exc_value, exc_tb):
    tb = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
    print("error catched!:")
    print("error message:\n", tb)
    warning("An unexpected serious error has occurred, check your file!")


def warning(txt):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setStyleSheet('background-color: rgb(80, 80, 80);')
    msgBox.setText(txt)
    msgBox.setWindowTitle("Error")
    msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    msgBox.exec_()


def not_ready(txt):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setStyleSheet('background-color: rgb(80, 80, 80);')
    msgBox.setText(txt)
    msgBox.setWindowTitle("Sorry :(")
    msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    msgBox.exec_()


sys.excepthook = excepthook


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Mywidget()
    ex.show()
    sys.exit(app.exec_())
