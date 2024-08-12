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

        # ip address format
        range = "(?:[0-1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])"
        ipRegex = QRegExp("^" + range + "\\." + range + "\\." + \
                          range + "\\." + range + "$")
        
        self.ipEdit.setValidator(QRegExpValidator(ipRegex, self))
        self.portEdit.setValidator(QIntValidator())

        self.setWindowTitle("TCP Client")

        self.ConnectBtn.clicked.connect(self.connect)

        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.timeout)

        self.format = Struct('@ii')

        self.IR_sensor_value = 0
    
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
            self.connected = False

    def timeout(self):
        self.updateData(34, 0)
    
    def updateData(self, pin, status):
        if self.connected == True:
            data = self.format.pack(pin, status)
            req = self.sock.send(data)
            rev = self.format.unpack(self.sock.recv(self.format.size))
            if rev[0] == 34:
                self.IR_sensor_value = rev[1]
                self.IR_sensor.setText(str(self.IR_sensor_value))
                if self.IR_sensor_value < 3900:
                    self.shelf_state.setText('loaded')
                else:
                     self.shelf_state.setText('unloaded')            
            print(rev)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()
    sys.exit(app.exec_())