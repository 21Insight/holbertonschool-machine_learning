#!/usr/bin/env python3
"""Module with Exponential class"""


class Normal:
    """Class that represents a normal distribution"""

    eu_num = 2.7182818285
    pi_num = 3.1415926536

    @staticmethod
    def get_stddev(data, mean):
        """Calculates Standard Deviation with a given data and mean"""
        summation = 0
        for number in data:
            summation += (number - mean) ** 2
        return (summation/len(data)) ** (1/2)

    @classmethod
    def get_erf(cls, x):
        seq = x - ((x ** 3)/3) + ((x ** 5)/10) - ((x ** 7)/42) + ((x ** 9)/216)
        erf = (2/(cls.pi_num ** (1/2))) * seq
        return erf

    def __init__(self, data=None, mean=0, stddev=1.):
        """Class constructor"""
        if data is not None:
            if not isinstance(data, list):
                raise TypeError('data must be a list')
            if len(data) < 2:
                raise ValueError('data must contain multiple values')
            self.mean = sum(data)/len(data)
            self.stddev = self.get_stddev(data, self.mean)
        else:
            if stddev <= 0:
                raise ValueError('stddev must be a positive value')
            self.mean = float(mean)
            self.stddev = float(stddev)

    def z_score(self, x):
        """Calculates z_score"""
        return (x - self.mean)/self.stddev

    def x_value(self, z):
        """Calculates x_value"""
        return (z * self.stddev) + self.mean

    def pdf(self, x):
        """Calculates Probability Density Function (PDF)"""
        exp_component = (-1/2) * (((x - self.mean)/self.stddev) ** 2)
        euler_exp = self.eu_num ** exp_component
        cdf = euler_exp/(self.stddev * ((2 * self.pi_num) ** (1/2)))
        return cdf

    def cdf(self, x):
        """Calculates Cumulative Distribution Function (CDF)"""
        expression = (x - self.mean)/(self.stddev * (2 ** (1/2)))
        return (1/2) * (1 + self.get_erf(expression))
