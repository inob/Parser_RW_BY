import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
import requests
from bs4 import BeautifulSoup
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5 import QtGui

class Menu(QDialog):
    def __init__(self):
        super(Menu,self).__init__()
        loadUi("menu.ui",self)
        self.pushButton.clicked.connect(self.ParsingF)
    
    def ParsingF(self):
        place1 = self.lineEdit.text()
        place2 = self.lineEdit_2.text()
        date = str(self.dateEdit.text())
        times = str(self.timeEdit.text())
        print(place1, place2, date, times)
        self.textBrowser.append(place1 + "\n ---> \n" + place2)


app=QApplication(sys.argv)
mainwindow=Menu()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(600)
widget.setFixedHeight(400)
widget.setWindowTitle("Crypto")
widget.show()
app.exec_()