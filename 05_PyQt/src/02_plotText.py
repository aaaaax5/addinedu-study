import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

# ui 파일 연결 - 코드 파일과 같은 폴더내에 위치하여야함
from_class = uic.loadUiType("02_plotText.ui")[0]

#화면 클래스
class WindowClass(QMainWindow, from_class) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle("Test Qt!")
        self.textEdit.setText("This is Text editor.")

#Python Main 함수
if __name__ == "__main__":
    app = QApplication(sys.argv)    #프로그램 실행
    myWindows = WindowClass()       #화면 클래스 생성
    myWindows.show()                #프로그램 화면 보이기
    sys.exit(app.exec_())           #프로그램을 종료까지 동화시킴