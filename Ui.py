from PyQt5 import uic
import sys
from PyQt5 import QtWidgets as QW



app = QW.QApplication(sys.argv)
window = uic.loadUi("main_window.ui")

window.show()
app.exec_()

