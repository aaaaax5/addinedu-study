import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

# ui 파일 연결 - 코드 파일과 같은 폴더내에 위치하여야함
from_class = uic.loadUiType("08.01_comboBox_tableWidget.ui")[0]

#화면 클래스
class WindowClass(QMainWindow, from_class) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        for year in range(1900, 2022 + 1):
            self.cbYear.addItem(str(year))

        for month in range(1, 12 + 1):
            self.cbMonth.addItem(str(month))
        
        for day in range(1, 31 + 1):
            self.cbDay.addItem(str(day))
        
        self.cbYear.setCurrentText(str(1990))
        self.cbDay.currentIndexChanged.connect(self.printBirthday)
        self.calendarWidget.clicked.connect(self.selectDate)

    def printBirthday(self):
        year = self.cbYear.currentText()
        month = self.cbMonth.currentText()
        day = self.cbDay.currentText()
        self.lineEdit.setText(year + month.zfill(2) + day.zfill(2))
    
    def selectDate(self):
        date = self.calendarWidget.selectedDate()
        year = date.toString('yyyy')
        month = date.toString('M')
        day = date.toString('d')

        self.cbYear.setCurrentText(year)
        self.cbMonth.setCurrentText(month)
        self.cbDay.setCurrentText(day)
        self.lineEdit.setText(year + month.zfill(2) + day.zfill(2))

#Python Main 함수
if __name__ == "__main__":
    app = QApplication(sys.argv)    #프로그램 실행
    myWindows = WindowClass()       #화면 클래스 생성
    myWindows.show()                #프로그램 화면 보이기
    sys.exit(app.exec_())           #프로그램을 종료까지 동화시킴