import sys
from PyQt5 import uic, QtGui, QtCore 
from PyQt5 import QtWidgets as QW
import Weather
def convertTuple(tup): 
    x =  " ".join(str(tup)) 
    return str(x)

class MainWindow(QW.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        uic.loadUi("main_window.ui",self)
        
        self.pushButton.clicked.connect(self.clickedBtn)

    def clickedBtn(self):
        place = self.textEdit.toPlainText()
        place_lc = place.lower()
        self.result_text.setPlainText(convertTuple(Weather.getWeatherAtPlace(place_lc)))


app = QW.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()

