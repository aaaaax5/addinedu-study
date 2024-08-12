import sys
from PyQt5.QtCore import Qt, QLine, QPoint
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
import urllib.request

from_class = uic.loadUiType("11_painter.ui")[0]

class WindowClass(QMainWindow, from_class) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pixmap = QPixmap(self.label.width(), self.label.height())
        self.pixmap.fill(Qt.white)

        self.label.setPixmap(self.pixmap)
        self.x, self.y = None, None
        # self.draw()
    
    def mouseMoveEvent(self, event):
        if self.x is None:
            self.x = event.x()
            self.y = event.y()
            return
        
        painter = QPainter(self.label.pixmap())
        painter.drawLine(self.x - self.label.x(), self.y - self.label.y(),
                          event.x() - self.label.x(), event.y() - self.label.y()
                          )
        painter.end()
        self.update()

        self.x = event.x()
        self.y = event.y()

    def mouseReleaseEvent(self, event):
        self.x = None
        self.y = None
    
    def draw(self):
        painter = QPainter(self.label.pixmap())
        painter.setPen(QPen(Qt.blue, 5, Qt.SolidLine))

        self.font = QFont()
        self.font.setFamily('Times')
        self.font.setBold(True)
        self.font.setPointSize(20)
        painter.setFont(self.font)
        
        painter.drawText(100, 100, 'This is drawText.')
        painter.end()

    def drawSet(self):
        painter = QPainter(self.label.pixmap())

        self.pen = QPen(Qt.red, 5, Qt.SolidLine)
        painter.setPen(self.pen)
        painter.drawLine(100,100,500,100)

        self.pen = QPen(Qt.blue, 10, Qt.DashDotLine)
        painter.setPen(self.pen)
        self.line = QLine(100,200,500,200)
        painter.drawLine(self.line)

        painter.setPen(QPen(Qt.black, 20, Qt.DotLine))
        self.p1 = QPoint(100, 300)
        self.p2 = QPoint(500, 300)
        painter.drawLine(self.p1, self.p2)

        painter = QPainter(self.label.pixmap())
        painter.setPen(QPen(Qt.red, 20, Qt.SolidLine))
        painter.drawPoint(100,100)

        painter.setPen(QPen(Qt.red, 5, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.black))
        painter.drawRect(100, 100, 100, 100)

        painter.setPen(QPen(Qt.red, 5, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.black))
        painter.drawEllipse(100, 100, 100, 100)

        painter.end()

    def drawText(self):
        painter = QPainter(self.label.pixmap())
        painter.setPen(QPen(Qt.blue, 5, Qt.SolidLine))

        self.font = QFont()
        self.font.setFamily('Times')
        self.font.setBold(True)
        self.font.setPointSize(20)
        painter.setFont(self.font)
        
        painter.drawText(100, 100, 'This is drawText.')
        painter.end()
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()

    sys.exit(app.exec_())