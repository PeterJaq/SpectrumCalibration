import numpy
from Util.curve import Cruve

class Fitting:
    def __init__(self):
        self.mLinear = False
        self.mQuadratic = False
        self.mCubic = False
        self.mGauss = False
        self.peakPiexl = None
        self.peakWavelength = None

    def fittingLine(self):
        resultList = []
        workModel = [self.mLinear, self.mQuadratic, self.mCubic, self.mGauss]
        workModelName = ['line', 'square', 'cube', 'gauss']
        for model in range(0, len(workModel)):
            if workModel[model] is True:
                #resultList.append()
                cruve = Cruve(self.peakPiexl, self.peakWavelength)
                resultList.append(cruve.Fitting(model=workModelName[model]))
            else:
                resultList.append([0])

        #print(resultList)
        return resultList