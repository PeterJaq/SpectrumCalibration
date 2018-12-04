# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1364, 778)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.LoadButton = QtWidgets.QPushButton(self.centralwidget)
        self.LoadButton.setGeometry(QtCore.QRect(1240, 690, 111, 31))
        self.LoadButton.setObjectName("LoadButton")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(1100, 10, 251, 661))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(10, 20, 191, 16))
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox.setGeometry(QtCore.QRect(30, 500, 191, 141))
        self.groupBox.setObjectName("groupBox")
        self.LinearBox = QtWidgets.QCheckBox(self.groupBox)
        self.LinearBox.setGeometry(QtCore.QRect(10, 20, 71, 16))
        self.LinearBox.setObjectName("LinearBox")
        self.GaussBox = QtWidgets.QCheckBox(self.groupBox)
        self.GaussBox.setGeometry(QtCore.QRect(10, 110, 151, 16))
        self.GaussBox.setObjectName("GaussBox")
        self.QuadraticBox = QtWidgets.QCheckBox(self.groupBox)
        self.QuadraticBox.setGeometry(QtCore.QRect(10, 50, 171, 16))
        self.QuadraticBox.setObjectName("QuadraticBox")
        self.CubicBox = QtWidgets.QCheckBox(self.groupBox)
        self.CubicBox.setGeometry(QtCore.QRect(10, 80, 151, 16))
        self.CubicBox.setObjectName("CubicBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 141, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit.setGeometry(QtCore.QRect(10, 50, 221, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 110, 221, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.LoadButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.LoadButton_2.setGeometry(QtCore.QRect(1100, 690, 111, 31))
        self.LoadButton_2.setObjectName("LoadButton_2")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(460, 400, 621, 321))
        self.textEdit.setObjectName("textEdit")
        self.graphicsPixel = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsPixel.setGeometry(QtCore.QRect(20, 10, 1061, 381))
        self.graphicsPixel.setObjectName("graphicsPixel")
        self.graphicsRaw = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsRaw.setGeometry(QtCore.QRect(20, 400, 431, 321))
        self.graphicsRaw.setObjectName("graphicsRaw")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1364, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.LoadButton.setText(_translate("MainWindow", "Load Image"))
        self.groupBox_2.setTitle(_translate("MainWindow", "GroupBox"))
        self.label.setText(_translate("MainWindow", "Input peak piexl"))
        self.groupBox.setTitle(_translate("MainWindow", "Curve fitting method"))
        self.LinearBox.setText(_translate("MainWindow", "Linear"))
        self.GaussBox.setText(_translate("MainWindow", "Gauss"))
        self.QuadraticBox.setText(_translate("MainWindow", "Quadratic "))
        self.CubicBox.setText(_translate("MainWindow", "Cubic"))
        self.label_2.setText(_translate("MainWindow", "Input fit wavelength"))
        self.LoadButton_2.setText(_translate("MainWindow", "Next Line"))

