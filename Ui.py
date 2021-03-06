import sys
from PyQt5 import uic, QtGui, QtCore 
from PyQt5 import QtWidgets as QW
 
import Weather
import csv



autocomplete_cities = []
'''
with open("autocomplete_cities.csv",encoding = 'utf-8') as file:
    reader = csv.reader(file)
    first = True
    for row in reader:
        if first:
            first = False
            continue
        else:
            autocomplete_cities.append(row[0].lower())
 '''       
places = Weather.loadPlacesSQL()
for place in places:
    autocomplete_cities.append(place[0])




def convertTupleToString(tup): 
    x =  " ".join(str(tup)) 
    return str(x)

class MainWindow(QW.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        global autocomplete_cities
        self.ui = uic.loadUi("main_window_lmfao.ui",self)

        completer = QW.QCompleter(autocomplete_cities)
        searchbar = self.ui.findChild(QW.QLineEdit, "lineEdit")
        searchbar.setCompleter(completer)
        self.lineEdit.returnPressed.connect(self.clickedBtn)
        self.pushButton.clicked.connect(self.clickedBtn)
        self.pixmap = QtGui.QPixmap('/Users/nishchay/Github/weatherapp/Assets/104588-glitch_art-pixel_sorting-clouds.jpg')
        self.label_2.setPixmap(self.pixmap) 
        #self.saveButton.clicked.connect(self.saveBtn)

        self.saved_table_gui = self.ui.findChild(QW.QTableWidget,"tableWidget")
        atMaxLast10saved = Weather.loadSavedPlaces()
        '''
        r = 0
        for i in atMaxLast10saved:
            self.saved_table_gui.item(r,0).setText(i)
            
            r+=1
        '''

    def clickedBtn(self):
        place = self.lineEdit.text()
        place_lc = place.lower()
        weather_call_result = Weather.getWeatherAtPlace(place_lc)
        self.result_text.setPlainText(convertTupleToString(weather_call_result))
        
    
    
    def saveBtn(self):
        try:
            place = self.lineEdit.text()
            place_lc = place.lower()
            Weather.sqlObj.addToSaved(place_lc)
        except:
            if(Weather.checkIfActualPlace(place_lc)):
                Weather.sqlObj.addToPlaces(place_lc)
                Weather.sqlObj.addToSaved(place_lc)
            

        


app = QW.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
