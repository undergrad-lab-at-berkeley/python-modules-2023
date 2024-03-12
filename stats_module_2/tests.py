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

    def test_1b(self, bb):
        self.assertTrue(np.allclose(bb(397e-9,3e3,5,1), 338098126144))
        self.assertTrue(np.allclose(bb(397e-9,2e3,5,1), 799447237))
        self.assertTrue(np.allclose(bb(397e-9,1e3,5,1), 11.5691))

    def test_1c(self, t):
        self.assertTrue(5480<t<5520)

    def test_1f(self, t):
        self.assertTrue(520<t<530)

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
