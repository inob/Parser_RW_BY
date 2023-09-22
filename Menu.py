import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import telebot
from plyer import notification
import tokenTG
from datetime import datetime
import fake_useragent #Генерируем User-agent в заголовки

class Menu(QDialog):
    def __init__(self):
        super(Menu,self).__init__()
        loadUi("menu.ui",self)
        self.pushButton.clicked.connect(self.StartParsing)
    
    def StartParsing(self):
        place1 = self.lineEdit.text()
        place2 = self.lineEdit_2.text()
        date = str(self.dateEdit.text()).split(".")
        times = str(self.timeEdit.text())
        print(place1, place2, date, times)
        self.textBrowser.append(place1 + "\n ---> \n" + place2)
        url = f"https://pass.rw.by/ru/route/?from={place1}&from_exp=&from_esr=&to={place2}&to_exp=&to_esr=&date=20{date[2]}-{date[1]}-{date[0]}"
        print(date)
        self.Parsing(url, times)
        

    def Parsing(self, url, times):
        #####################################################################################################
        token=tokenTG.token         #Токен для бота
        MyID = tokenTG.IdInTelegram #Ваш Айди в Телеграмме(Узнать можно )
        #####################################################################################################
        bot =  telebot.TeleBot(token)

        agent = fake_useragent.UserAgent().random #Генерируем случайный User-agent
        option = webdriver.FirefoxOptions() #Настраиваем эмулятор браузера
        option.set_preference("dom.webdriver.enabled", False)
        option.set_preference("dom.webnotifications.enabled",False)
        option.set_preference("general.useragent.override",agent)
        option.add_argument('--headless') #Отвечает за скрытие работу эмулятора
        header = {
            "User-Agent":agent,
            "Accept":"*/*"
        }
        browser = webdriver.Firefox(options=option)
        while(True):
            try:
                browser.get(url)
                massiv_biletov = browser.find_elements(By.CLASS_NAME,"sch-table__row-wrap")

                MyTicket = self.check(massiv_biletov, times)
                exist = MyTicket.find_element(By.CLASS_NAME, "cell-4")
                print(exist.text)
                if  exist.text != "Мест нет":
                    now = datetime.now() 
                    current_time = now.strftime("%H:%M:%S") 
                    print( current_time, " - места появились " + MyTicket.text)
                    bot.send_message(MyID, "Появились места: " + MyTicket.text)
                    notification.notify(
                    title='Билет на поезд',
                    message='Места появились !')
                else:
                    now = datetime.now() 
                    current_time = now.strftime("%H:%M:%S") 
                    print("Мест нет: ", current_time)
                time.sleep(55)
            except:
                time.sleep(25)

    def check(self, massive, times):
        for i in massive:
            time_i = i.find_element(By.CLASS_NAME,"train-from-time").text
            print(f"---\n"+time_i)
            if time_i == times:
                return i



if __name__ == "__main__":
    app=QApplication(sys.argv)
    mainwindow=Menu()
    widget=QtWidgets.QStackedWidget()
    widget.addWidget(mainwindow)
    widget.setFixedWidth(600)
    widget.setFixedHeight(400)
    widget.setWindowTitle("Ticket")
    widget.show()
    app.exec_()