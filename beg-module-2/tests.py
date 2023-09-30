import math
import random
import __main__
import datetime
import unittest
import numpy as np
from IPython.display import Markdown, display

########## TESTS ##########
class Tests(unittest.TestCase):

    def test_1(self, ans):
        self.assertAlmostEqual(ans, 2021)

    def test_5a(self, v):
        three_fact = 3*2
        five_fact = 5*4*3*2
        val = 0.5 - (0.5**3)/three_fact + (0.5**5)/five_fact
        self.assertAlmostEqual(val, v)

    def test_5b(self, v):
        self.assertAlmostEqual(math.sin(0.5), v)
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
