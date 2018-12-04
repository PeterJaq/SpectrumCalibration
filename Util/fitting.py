import numpy

class Fitting:
    def __init__(self):
        self.mLinear = False
        self.mQuadratic = False
        self.mCubic = False
        self.mGauss = False
        self.peakPiexl = None
        self.peakWavelength = None
