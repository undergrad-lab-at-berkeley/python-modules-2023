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

    def test_1a(self, cols):
        self.assertTrue(np.allclose(cols, np.load('tests/1a.npy')))

    def test_1b(self, df):
        N = len(df)
        self.assertEquals(N, 118218) 
        self.assertTrue(np.alltrue(df.columns==['RAhms','DEdms','Plx','B-V','e_B-V','Hpmag']))
        
        def f(x):
            self.assertTrue(type(x)==str)
            return x.strip()
        strip = np.vectorize(f)
        self.assertTrue(np.alltrue(strip(df.iloc[0:1].to_numpy()) == ['00 00 00.22', '+01 05 20.4', '3.54', '0.482', '0.025', '9.2043']))
        self.assertTrue(np.alltrue(strip(df.iloc[N-1:N].to_numpy()) == ['23 59 54.91', '-65 34 37.5', '8.71', '-0.075', '0.011',
        '4.4758']))
        
    def test_1c(self, df):
        self.assertEquals(len(df), 118218)
        self.assertTrue(np.alltrue((df.dtypes.to_numpy()==float) == [False, False,  True,  True,  True,  True]))
        
    def test_1d(self, df):
        self.assertEquals(len(df), 116812)
        self.assertEquals(np.sum(np.sum(df.isnull()).to_numpy()), 0)
        

    def test_1e(self, df):
        self.assertEquals(len(df), 104099)
        self.assertEquals(np.sum(df['Plx']>0), 104099)
        self.assertEquals(np.sum(df['e_B-V']<0.05), 104099)


    def test_1f(self, df):
        self.assertEquals(len(df), 104099)
        self.assertTrue(np.allclose(df[df['Plx']==21.9]['Dist'].to_numpy(), 148.94977169))
        
    def test_1g(self, df):
        self.assertEquals(len(df), 104099)
        self.assertTrue(np.allclose(df[(df['Hpmag']==8.7077) & (df['Dist']<300)]['M'].to_numpy(), 4.05419006))

    def test_1h(self):
        self.assertTrue('my_hr.png' in os.listdir(os.getcwd()))    

    def test_2a(self, df):
        self.assertEquals(len(df), 104099)
        self.assertEquals(df.iloc[7:8].to_numpy()[0][0], '00 00 08.48')
        self.assertEquals(df.iloc[100:101].to_numpy()[0][0], '00 01 23.69')
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
