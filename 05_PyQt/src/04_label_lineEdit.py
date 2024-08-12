import sys
from PyQt5.QtCore import QEvent
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

# ui 파일 연결 - 코드 파일과 같은 폴더내에 위치하여야함
from_class = uic.loadUiType("04_label_lineEdit.ui")[0]

#화면 클래스
class WindowClass(QMainWindow, from_class) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Test2")

        self.count = 0
        self.pushButton.clicked.connect(self.buttonClicked)
        self.pushButton_2.clicked.connect(self.reset)
        self.pushButton_3.clicked.connect(self.write)

        self.label.setText(str(self.count))

        self.lineEdit_2.textChanged.connect(self.changed)

    def changed(self):
        self.lineEdit_3.setText(self.lineEdit_2.text())

    def write(self):
        self.label.setText(self.lineEdit.text())


    def buttonClicked(self) :
        self.count += 1
        self.label.setText(str(self.count))
    
    def reset(self):
        self.count = 0
        self.label.setText(str(self.count))

#Python Main 함수
if __name__ == "__main__":
    app = QApplication(sys.argv)    #프로그램 실행
    myWindows = WindowClass()       #화면 클래스 생성
    myWindows.show()                #프로그램 화면 보이기
    sys.exit(app.exec_())           #프로그램을 종료까지 동화시킴