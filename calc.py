from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage, QPixmap
from Util.ImageProcess import ImageProcess
from Util.fitting import Fitting
from UI.UI import Ui_MainWindow
import pyqtgraph as pg

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.imageProcess = ImageProcess()
        self.fitting = Fitting()

    #SIGNAL CONNECT

        self.LoadButton.clicked.connect(lambda: self.loadImage())
        self.LoadButton_2.clicked.connect(lambda: self.nextData())
        self.LinearBox.stateChanged.connect(lambda: self.changeLinearBox())
        self.QuadraticBox.stateChanged.connect(lambda: self.changeQuadraticBox())
        self.CubicBox.stateChanged.connect(lambda: self.changeCubicBox())
        self.GaussBox.stateChanged.connect(lambda: self.changeGaussBox())
        self.spinBox_x.valueChanged.connect(lambda: self.changeStartPixel())
        self.spinBox_y.valueChanged.connect(lambda: self.changeEndPixel())

    #SLOT

    def loadImage(self):
        Filter = "PNG (*.png);; JPG (*.jpg);; TIF(*.tif)"
        FileName = QtWidgets.QFileDialog.getOpenFileName(self, "Input Image", "", Filter)

        self.imageProcess.set_file_name(FileName)
        img = self.imageProcess.load_img_data()
        Qimg = QImage(FileName[0])
        self.label_3.setPixmap(QPixmap(Qimg))

    def nextData(self):
        self.imageProcess.loadLine += 1
        LineData = self.imageProcess.imgData[self.imageProcess.loadLine][self.imageProcess.startPixel: self.imageProcess.endPixel]
        x = [i for i in range(self.imageProcess.startPixel, self.imageProcess.endPixel)]
        plot = pg.PlotWidget()
        p1 = plot.plotItem
        p1.addItem(pg.PlotCurveItem(x=x, y=LineData))
        self.gridLayout.addWidget(plot, 0, 1)


    def changeLinearBox(self):
        self.fitting.mLinear = True if self.LinearBox.checkState() == 2 else False
        #print(self.fitting.mLinear)

    def changeQuadraticBox(self):
        self.fitting.mQuadratic = True if self.QuadraticBox.checkState() == 2 else False

    def changeCubicBox(self):
        self.fitting.mCubic = True if self.CubicBox.checkState() == 2 else False

    def changeGaussBox(self):
        self.fitting.mGauss = True if self.GaussBox.checkState() == 2 else False

    def changeStartPixel(self):
        self.imageProcess.startPixel = self.spinBox_x.value()

    def changeEndPixel(self):
        self.imageProcess.endPixel = self.spinBox_y.value()
