import sys
from PyQt5 import uic, QtGui, QtCore 
from PyQt5 import QtWidgets as QW
import Weather
import csv


autocomplete_cities = []
with open("autocomplete_cities.csv",encoding = 'utf-8') as file:
    reader = csv.reader(file)
    first = True
    for row in reader:
        if first:
            first = False
            continue
        else:
            autocomplete_cities.append(row[0].lower())



def convertTupleToString(tup): 
    x =  " ".join(str(tup)) 
    return str(x)

class MainWindow(QW.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.ui = uic.loadUi("main_window.ui",self)
        

        completer = QW.QCompleter(autocomplete_cities)
        searchbar = self.ui.findChild(QW.QLineEdit, "lineEdit")
        searchbar.setCompleter(completer)
        #uncomment the above line once you find a way to use QW.QLineEdit instead of QW.QTextEdit for searchbar
        #only then can it use the completer


        self.pushButton.clicked.connect(self.clickedBtn)
        self.saveButton.clicked.connect(self.saveBtn)


    def clickedBtn(self):
        place = self.lineEdit.text()
        place_lc = place.lower()
        weather_call_result = Weather.getWeatherAtPlace(place_lc)
        self.result_text.setPlainText(convertTupleToString(weather_call_result))
        
    
    def saveBtn(self):
        '''
        entering soon
        '''


app = QW.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()