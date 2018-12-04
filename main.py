import sys
from PyQt5 import QtWidgets
from UI.UI import Ui_MainWindow
from calc import MainWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
