import cv2
import numpy as np


class ImageProcess:

    def __init__(self):
        self.FileName = ""
        self.img = None
        self.imgData = None
        self.imgShape = None
        self.loadLine = 0
        self.startPixel = 0
        self.endPixel = 2047

    def set_file_name(self, file_name):
        self.FileName = file_name

    def load_img_data(self):
        self.img = cv2.imread(self.FileName[0], cv2.CV_16UC1)
        print(self.img.strides)
        self.imgShape = self.img.shape
        self.imgData = np.array(self.img)
        print(self.imgData)

    def get_img(self):
        return self.img, cv2.COLOR

    def get_img_data(self):

        return self.imgData

    def get_file_name(self):
        return self.FileName

