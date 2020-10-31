from PyQt5 import uic
import sys
from PyQt5 import QtWidgets as QW


class UI(QW.QMainWindow):
    def __init__(self):
        super(UI,self).__init__()
        uic.loadUi("main_window.ui",self)


        self.textedit = self.findChild(QW.QTextEdit,"textEdit")
        self.label = self.findChild(QW.QLabel,"label")
        self.tabwidget = self.findChild(QW.QTabWidget,"tabWidget")




app = QW.QApplication(sys.argv)
window = UI()
app.exec_()