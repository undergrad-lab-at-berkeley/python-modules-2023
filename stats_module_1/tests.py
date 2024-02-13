import math
import random
import __main__
import datetime
import unittest
import numpy as np
import pandas as pd
from IPython.display import Markdown, display
import os

pi = np.pi
g = 9.81

########## TESTS ##########
class Tests(unittest.TestCase):

    def test_1a(self, h):
        self.assertTrue(type(h)==np.ndarray)
        self.assertTrue(h.shape==(500,))
        self.assertTrue(np.min(h)==85.4)
        self.assertTrue(np.max(h)==144.4)

    def test_1e(self, p):
        self.assertTrue(np.allclose(p, 0.828))

    def test_1f(self, p):
        self.assertTrue(np.allclose(p, 0.829, atol=1e-3))

    def test_2a(self, poisson):
        x = []
        for i in range(1000):
            x.append(poisson(50,1,10000))
        # mean and var of possion(x) is x
        self.assertTrue(49.5<np.mean(x)<50.5)
        self.assertTrue(6.5<np.std(x)<7.5)

    def test_2b(self, x):
        self.assertTrue(49.5<np.mean(x)<50.5)
        self.assertTrue(6.5<np.std(x)<7.5)
####################


def printmd(string):
    display(Markdown(string))

tests = Tests()

def run(test_name, *args, hint=False):
    dt = datetime.datetime.now()
    try:
        getattr(tests, test_name)(*args)
    except tests.failureException as e:
        printmd(f'**<span style="color: red;">Failed // {dt}</span>**')
        if hint:
            print('Hint:',  e)
        return
    printmd(f'**<span style="color: green;">Passed // {dt}</span>**')
