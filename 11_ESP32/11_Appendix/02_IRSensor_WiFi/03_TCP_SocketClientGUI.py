import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5.QtCore import *
import socket
from struct import *
import datetime

from_class = uic.loadUiType("09_TCP_SocketClientGUI.ui")[0]

class WindowClass(QMainWindow, from_class) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # flag
        self.connectTCP = False
        self.connected = False

        # timer
        self.timer = QTimer(self)
        self.timer.start(500)

        # ip address format
        range = "(?:[0-1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])"
        ipRegex = QRegExp("^" + range + "\\." + range + "\\." + \
                          range + "\\." + range + "$")
        
        self.ipEdit.setValidator(QRegExpValidator(ipRegex, self))
        self.portEdit.setValidator(QIntValidator())
        self.degree.setValidator(QIntValidator())

        self.setWindowTitle("TCP Client")

        self.ConnectBtn.clicked.connect(self.connect)
        self.led21.clicked.connect(self.clickLED21)
        self.led22.clicked.connect(self.clickLED22)
        self.led23.clicked.connect(self.clickLED23)
        self.move.clicked.connect(self.clickMove)
        self.timer.timeout.connect(self.timeout)
    
    def __del__(self):
        self.sock.close()
        self.connected = False

    def connect(self):
        if self.connectTCP == False:
            ip = self. ipEdit.text()
            port = self.portEdit.text()
            self.sock = socket.socket()
            self.sock.connect((ip, int(port)))
            self.ConnectBtn.setText('Disconnect')
            self.connectTCP = True
            self.connected = True
        else:
            self.sock.close()
            self.ConnectBtn.setText('Connect')
            self.connectTCP = False

        
        self.format = Struct('@ii')
        #message practice
        # message = "Hello TCP/IP!"
        # self.sock.send(message.encode())
        # data = ""
        # while len(data) < len(message):
        #     data += self.sock.recv(1).decode()

        # print(data)


    def clickLED21(self):
        isOn = self.led21.isChecked()
        self.updateLED(21, isOn)

    def clickLED22(self):
        isOn = self.led22.isChecked()
        self.updateLED(22, isOn)

    def clickLED23(self):
        isOn = self.led23.isChecked()
        self.updateLED(23, isOn)

    def clickMove(self):
        degree = int(self.degree.text())
        self.updateLED(5, degree)

    def updateLED(self, pin, status):
        data = self.format.pack(pin, status)
        req = self.sock.send(data)
        rev = self.format.unpack(self.sock.recv(self.format.size))
        test = unpack('@ii', data)
        print(test)
    
    def timeout(self):
        self.updateLED(34, 0)
    
    def updateLED(self, pin, status):
        if self.connected == True:
            data = self.format.pack(pin, status)
            req = self.sock.send(data)
            rev = self.format.unpack(self.sock.recv(self.format.size))
            if rev[0] == 34:
                self.photoresistor.setText(str(rev[1]))
            
            print(rev)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()
    sys.exit(app.exec_())