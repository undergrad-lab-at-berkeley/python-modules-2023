import math
import random
import __main__
import datetime
import unittest
import numpy as np
from IPython.display import Markdown, display

########## TESTS ##########
class Tests(unittest.TestCase):

    def test_1(self, exponential):
        np.random.seed(3)
        self.assertTrue(np.isclose(np.e, exponential(1))) 
        for _ in range(10):
            x = np.random.randn()
            self.assertTrue(np.isclose(np.exp(x), exponential(x), atol=1e-4))

    def test_2(self, positions):
        lengths = [1, 3, 4]
        pi = np.pi
        thetas = [pi / 4, -pi / 3, pi / 6]
        pos = positions(thetas, lengths)
        self.assertTrue(np.allclose(
            pos,
            np.array([[ 0.70710678, -0.70710678],
                      [-1.89096943, -2.20710678],
                      [ 0.10903057, -5.6712084 ]])))
        self.assertTrue(type(pos)==np.ndarray)

    def test_3(self, get_accel_1):
        pi = np.pi
        angle = -pi / 3
        vel = pi / 12
        length = 1
        m = 1
        print(get_accel_1(angle, vel, length, m))
        self.assertTrue(np.isclose(get_accel_1(angle, vel, length, m), 8.495709))
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
