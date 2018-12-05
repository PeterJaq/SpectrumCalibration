import numpy as np
from scipy import optimize
import math


class Cruve:

    def __init__(self, x_0, y_0):
        self.x_0 = x_0
        self.y_0 = y_0

    def f_1(self, x, A, B):
        return A * x + B

    # 二次曲线方程
    def f_2(self, x, A, B, C):
        return A * x * x + B * x + C

    # 三次曲线方程
    def f_3(self, x, A, B, C, D):
        return A * x * x * x + B * x * x + C * x + D

    def f_gauss(self, x, A, B, C, sigma):
        return A * np.exp(-(x - B) ** 2 / (2 * sigma ** 2)) + C

    def f_ln(self, x, A, B):
        return A * np.log(x) + B

    def Fitting(self, model="line"):

        info = []

        if model is "line":
            A1, B1 = optimize.curve_fit(self.f_1, self.x_0, self.y_0)[0]
            info = [A1, B1]
            #y_1 = A1 * self.x_1 + B1

        elif model is "square":
            A1, B1, C1 = optimize.curve_fit(self.f_2, self.x_0, self.y_0)[0]
            info = [A1, B1, C1]
            #y_1 = A1 * self.x_1 * self.x_1 + B1*self.x_1 + C1

        elif model is "cube":
            A1, B1, C1, D1 = optimize.curve_fit(self.f_3, self.x_0, self.y_0)[0]
            info = [A1, B1, C1, D1]
            #y_1 = A1 * self.x_1 * self.x_1 * self.x_1 + B1 * self.x_1 * self.x_1 + C1* self.x_1 + D1

        elif model is "gauss":
            A1, B1, C1, sigma = optimize.curve_fit(self.f_gauss, self.x_0, self.y_0)[0]
            info = [A1, B1, C1, sigma]
            #y_1 = A1 * np.exp(-(self.x_1 - B1) ** 2 / (2 * sigma ** 2)) + C1

        elif model is "ln":
            A1, B1 = optimize.curve_fit(self.f_ln, self.x_0, self.y_0)[0]
            info = [A1, B1]
            #y_1 = A1 * np.log(self.x_1) + B1

        return info