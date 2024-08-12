import sys
import mysql.connector
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QApplication, QDateEdit

# ui 파일 연결 - 코드 파일과 같은 폴더내에 위치하여야함
from_class = uic.loadUiType("09.02_celcbTable_SQL.ui")[0]

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "0523",
    database = "amrbase"
)

#화면 클래스
class WindowClass(QMainWindow, from_class) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        ### connect mySQL
        cur = mydb.cursor()

        ### birthday min/max from celeb
        cur.execute("SELECT MIN(BIRTHDAY), MAX(BIRTHDAY) FROM celeb")
        result = cur.fetchone()
        self.min = result[0]
        self.max = result[1]

        self.dateStart.setDate(self.min)
        self.dateEnd.setDate(self.max)


        ### sex list from celeb
        cur.execute("SELECT DISTINCT SEX FROM celeb")
        sex_list = [row[0] for row in cur.fetchall()]
        self.cbSex.addItem('All')
        for sex in sex_list:
            self.cbSex.addItem(str(sex))
        
        ### JobTitle list from celeb
        cur.execute("SELECT DISTINCT JOB_TITLE FROM celeb")
        Job_list = [row[0] for row in cur.fetchall()]
        kind_of_job = []
        ## split ', ' and check duplicate         
        for Job_element in Job_list:
            jobs = Job_element.split(', ')
            for a_job in jobs:
                if a_job not in kind_of_job:
                    kind_of_job.append(a_job)

        self.cbJobTitle.addItem('All')
        for job in kind_of_job:
            self.cbJobTitle.addItem(str(job))

        # Agency list from celeb
        cur.execute("SELECT DISTINCT AGENCY FROM celeb")
        Agency_list = [row[0] for row in cur.fetchall()]
        self.cbAgency.addItem('All')
        for Agency in Agency_list:
            self.cbAgency.addItem(str(Agency))

        #if A start day is later than end day, warning pop up

#Python Main 함수
if __name__ == "__main__":
    app = QApplication(sys.argv)    #프로그램 실행
    myWindows = WindowClass()       #화면 클래스 생성
    myWindows.show()                #프로그램 화면 보이기

    sys.exit(app.exec_())           #프로그램을 종료까지 동화시킴