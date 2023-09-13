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
        self.place1
        self.password
        self.pushButton.clicked.connect(self.ParsingF)
    
    def ParsingF(self):
        pass



app=QApplication(sys.argv)
mainwindow=Menu()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setWindowTitle("Crypto")
widget.show()
app.exec_()  