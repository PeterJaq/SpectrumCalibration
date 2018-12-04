# Calibration the Spectrum

This is a Spectrum calibration software, build by PyQt5. The Spectrum is based on
2D CMOS sensor.

## requirment

```
PyQt5 >= 5.11
PyQt5-tools >= 5.11
numpy
```

## Author and supporter:

Jiang anqing from Waseda Univ. Japan, Fukuoka Email:anqingjiang0524@akane.waseda.jp

The project support by L.Y Chen from Fudan Univ. China, Shanghai

## Appendix:

If you need do any change to this program using Qdesigner, please consider add this follow code on the UI.py

```python
class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
```

