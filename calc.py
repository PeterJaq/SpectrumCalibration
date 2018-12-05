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
        self.FittingButton.clicked.connect(lambda: self.fittingCanvas())
        self.ChangeLineBox.valueChanged.connect(lambda: self.changeLine())


    #SLOT

    def loadImage(self):
        Filter = "PNG (*.png);; JPG (*.jpg);; TIF(*.tif)"
        FileName = QtWidgets.QFileDialog.getOpenFileName(self, "Input Image", "", Filter)

        self.imageProcess.set_file_name(FileName)
        lasize = self.label_3.size()
        img = self.imageProcess.load_img_data()
        Qimg = QImage(FileName[0]).scaled(lasize, aspectRatioMode=False)
        self.label_3.setPixmap(QPixmap(Qimg))

    def nextData(self):
        LineData = self.imageProcess.imgData[self.imageProcess.loadLine][self.imageProcess.startPixel: self.imageProcess.endPixel]
        x = [i for i in range(self.imageProcess.startPixel, self.imageProcess.endPixel)]
        self.p1 = pg.PlotWidget()
        self.p1.addItem(pg.PlotCurveItem(x=x, y=LineData))
        self.vLine = pg.InfiniteLine(angle=90, movable=False, label='{value:0.1f}',
                                        labelOpts={'position':0.98, 'color': (255,255,0), 'movable': True, 'fill': (0, 0, 0, 100)})
        self.hLine = pg.InfiniteLine(angle=0, movable=False)
        self.p1.addItem(self.vLine, ignoreBounds=True)
        self.p1.addItem(self.hLine, ignoreBounds=True)
        self.gridLayout.addWidget(self.p1, 0, 1)
        self.massageStatusBar(lineInfo = self.imageProcess.loadLine)
        self.imageProcess.loadLine += 1
        self.ChangeLineBox.setValue(self.imageProcess.loadLine)
        self.setMouseTracking(True)
        self.p1.scene().sigMouseMoved.connect(self.mouseMoved)

    def mouseMoved(self, evt):
        pos = evt
        if self.p1.sceneBoundingRect().contains(pos):
            mousePoint = self.p1.plotItem.vb.mapSceneToView(pos)
            #self.label_6.setText(
            #    "<span style='font-size: 15pt'>X=%0.1f, <span style='color: black'>Y=%0.1f</span>" % (
            #    mousePoint.x(), mousePoint.y()))
            self.vLine.setPos(mousePoint.x())
            self.hLine.setPos(mousePoint.y())
        #self.p1.plotItem(self.hLine.setPos(mousePoint.y()))

    def fittingCanvas(self):
        self.fitting.peakPiexl = [float(x) for x in self.lineEdit.text().split(' ')]
        print(self.lineEdit_2.text())
        self.fitting.peakWavelength = [float(x) for x in self.lineEdit_2.text().split(' ')]
        if len(self.fitting.peakPiexl) != len(self.fitting.peakWavelength):
            QtWidgets.QMessageBox.information(self, "提醒", "输入的波长及像素点未对应，不会进行拟合",
                                    QtWidgets.QMessageBox.Yes)
            return False

        lineResult = self.fitting.fittingLine()
        self.saveData(self.imageProcess.loadLine, lineResult)
        self.showInTest(self.imageProcess.loadLine, lineResult)

    def changeLine(self):
        self.imageProcess.loadLine = self.ChangeLineBox.value()

    def massageStatusBar(self, lineInfo=0):
        massage = "Line: %s " % lineInfo
        self.label_6.setText(massage)

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

    #normal function

    def saveData(self, line, result_data):
        if(self.fitting.mLinear is True):
            result_data_s = [str(x) for x in result_data[0]]
            f_l = open('./data/linear.txt', 'w+')
            writeInfo = str(line) + ' ' + ' '.join(result_data_s)
            f_l.writelines(writeInfo)
        if(self.fitting.mQuadratic is True):
            result_data_s = [str(x) for x in result_data[1]]
            f_q = open('./data/quadratic.txt', 'w+')
            writeInfo = str(line) + ' ' + ' '.join(result_data_s)
            f_q.writelines(writeInfo)
        if(self.fitting.mCubic is True):
            result_data_s = [str(x) for x in result_data[2]]
            f_c = open('./data/cubic.txt', 'w+')
            writeInfo = str(line) + ' ' + ' '.join(result_data_s)
            f_c.writelines(writeInfo)
        if(self.fitting.mGauss is True):
            result_data_s = [str(x) for x in result_data[3]]
            f_g = open('./data/gauss.txt', 'w+')
            writeInfo = str(line) + ' ' + ' '.join(result_data_s)
            f_g.writelines(writeInfo)

    def showInTest(self, line, result_data):
        if (self.fitting.mLinear is True):
            result_data_s = [str(x) for x in result_data[0]]
            writeInfo = str(line) + ' ' + ' '.join(result_data_s)
            self.textEdit.append(writeInfo)
        if(self.fitting.mQuadratic is True):
            result_data_s = [str(x) for x in result_data[1]]
            writeInfo = str(line) + ' ' + ' '.join(result_data_s)
            self.textEdit.append(writeInfo)
        if(self.fitting.mCubic is True):
            result_data_s = [str(x) for x in result_data[2]]
            writeInfo = str(line) + ' ' + ' '.join(result_data_s)
            self.textEdit.append(writeInfo)
        if(self.fitting.mGauss is True):
            result_data_s = [str(x) for x in result_data[3]]
            writeInfo = str(line) + ' ' + ' '.join(result_data_s)
            self.textEdit.append(writeInfo)

