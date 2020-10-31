from PyQt5 import uic
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QTextEdit, QLabel, QTabWidget


class UI(QMainWindow):
    def __init__(self):
        super(UI,self).__init__()
        uic.loadUi("main_window.ui",self)


        self.textedit = self.findChild(QTextEdit,"textEdit")
        self.label = self.findChild(QLabel,"label")
        self.tabwidget = self.findChild(QTabWidget,"tabWidget")




app = QApplication(sys.argv)
window = UI()
app.exec_()