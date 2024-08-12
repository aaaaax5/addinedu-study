import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget
import urllib.request

from_class = uic.loadUiType("10_spinBox_slider_pixMap.ui")[0]

class WindowClass(QMainWindow, from_class) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        min = self.spinBox.minimum()
        max = self.spinBox.maximum()
        step = self.spinBox.singleStep()

        self.editMin.setText(str(min))
        self.editMax.setText(str(max))
        self.editStep.setText(str(step))

        self.slider.setRange(min, max)
        self.slider.setSingleStep(step)

        self.btnApply.clicked.connect(self.apply)
        self.spinBox.valueChanged.connect(self.changeSpinBox)
        self.slider.valueChanged.connect(self.changeSlider)

        self.btnApply.clicked.connect(self.apply)
        self.spinBox.valueChanged.connect(self.changeSpinBox)
        self.slider.valueChanged.connect(self.changeSlider)

        self.btnSave.clicked.connect(self.saveImage)
        self.btnLoad.clicked.connect(self.openFile)


        url = "https://imageio.forbes.com/specials-images/imageserve/61b1f75e9bdd78e1c08fdd64/A-funny-labrador-dog-with-a-curiously-placed-bubble-in-its-behind-/0x0.jpg?format=jpg&crop=922,956,x0,y279,safe&width=1440"
        image = urllib.request.urlopen(url).read()

        self.pixmap = QPixmap()
        self.pixmap.loadFromData(image)

        self.pixmap = self.pixmap.scaled(self.labelPixmap.width(), self.labelPixmap.height())
        self.labelPixmap.setPixmap(self.pixmap)

        self.labelPixmap.setPixmap(self.pixmap)

    def apply(self):
        min = self.editMin.text()
        max = self.editMax.text()
        step = self.editStep.text()

        self.spinBox.setRange(int(min), int(max))
        self.spinBox.setSingleStep(int(step))

        self.slider.setRange(int(min), int(max))
        self.slider.setSingleStep(int(step))

    def changeSpinBox(self):
        actualValue = self.spinBox.value()
        self.labelValue.setText(str(actualValue))
        self.spinBox.setValue(actualValue)

    def changeSlider(self):
        actualValue = self.slider.value()
        self.labelValue2.setText(str(actualValue))
        self.slider.setValue(actualValue)
        

    def openFile(self):
        name = QFileDialog.getSaveFileName(self,
                                           "data/untitled.png")
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()

    sys.exit(app.exec_())