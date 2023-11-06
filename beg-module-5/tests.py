import math
import random
import __main__
import datetime
import unittest
import numpy as np
from IPython.display import Markdown, display

########## TESTS ##########
class Tests(unittest.TestCase):

    def test_0a(self, f):
        self.assertAlmostEqual(f[0], 0)
        self.assertAlmostEqual(f[1], 2.26762512e-05)
        self.assertAlmostEqual(f[2], 4.53525023e-05)
        self.assertEquals(len(f), 44100*2)

    def test_1a(self, a, b):
        self.assertEquals(len(a), 82176)
        self.assertEquals(len(b), 82176)
        self.assertAlmostEqual(a[0], 0)
        self.assertAlmostEqual(a[1], 2.68326519e-01)
        self.assertAlmostEqual(a[2], 5.36653037e-01)
        self.assertAlmostEqual(b[0], 67485)
        self.assertAlmostEqual(b[1], 60181.15921837)
        self.assertAlmostEqual(b[2], 66671.61369114)

    def test_1b(self, f, g):
        a = [31249467.94003125, 31825928.47394149, 36861778.0789194,  58474893.85028187, 28539743.10017001,  7463365.60219829,  7079510.01874627]
        self.assertEquals(len(a), len(f))
        a = np.sort(a)
        f = np.sort(f)
        for i in range(len(a)):
            self.assertAlmostEqual(f[i], a[i])
        self.assertAlmostEqual(g, 58474893.85028187)
    def test_mine(self, f):
        self.assertAlmostEqual(f[0], 0)
        self.assertAlmostEqual(f[1], 0.84147098)
        self.assertAlmostEqual(f[8], 0.98935825)
        self.assertAlmostEqual(f[9], 0.41211849)
        
    def test_mine2(self, f):
        self.assertEquals(f[0], True)
        self.assertEquals(f[1], False)
        self.assertEquals(f[2], True)
        self.assertEquals(f[3], True)
        self.assertEquals(f[4], True)
        self.assertEquals(f[5], False)





########## TESTS ##########


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


