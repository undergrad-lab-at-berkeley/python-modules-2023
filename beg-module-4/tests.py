import math
import random
import __main__
import datetime
import unittest
import numpy as np
from IPython.display import Markdown, display

########## TESTS ##########
class Tests(unittest.TestCase):

    def test_1(self, f):
        l1 = [1, 2, 3, 3, 4, 3, 3]
        l2 = [3, 1, 4, 5, 3, 4, 1]
        l3 = [1, 1, 1, 2, 3, 3, 3]

        self.assertEquals(f(l1, 3), [1, 2, 3, 4, 3, 3])
        self.assertEquals(f(l2, 3), [3, 1, 4, 5, 4, 1])
        self.assertEquals(f(l2, 1), [3, 1, 4, 5, 3, 4])
        self.assertEquals(f(l3, 1), [1, 1, 2, 3, 3, 3])
        self.assertEquals(f(l3, 3), [1, 1, 1, 2, 3, 3])

    def test_2(self, f):
        self.assertEquals(f, [1, 5, 9, 15, 21])

    def test_3(self, f):
        self.assertEquals(f, ['koi_gmag_err', 'koi_rmag_err', 'koi_imag_err', 'koi_zmag_err', 'koi_jmag_err', 'koi_hmag_err', 'koi_kmag_err', 'koi_kepmag_err', 'koi_fwm_sra_err', 'koi_fwm_sdec_err', 'koi_fwm_srao_err', 'koi_fwm_sdeco_err', 'koi_fwm_prao_err', 'koi_fwm_pdeco_err', 'koi_dicco_mra_err', 'koi_dicco_mdec_err', 'koi_dicco_msky_err', 'koi_dikco_mra_err', 'koi_dikco_mdec_err', 'koi_dikco_msky_err'])
    
    def test_4(self, f):
        self.assertEquals(f, 694)

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


