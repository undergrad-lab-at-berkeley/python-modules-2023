import math
import random
import __main__
import datetime
import unittest
import numpy as np
from IPython.display import Markdown, display


########## TESTS ##########
class Tests(unittest.TestCase):

    def test_0(self, f):
        def aqi_verbose(aqi):
            if aqi<=150:
                return f'The air quality is acceptable and {150-aqi} points from being unhealthy.'
            elif aqi<=300:
                return f'The air quality is unhealthy and {300-aqi} points from being hazardous.'
            else:
                return 'The air quality is hazardous.'

        for i in range(30):
            a = random.randint(0, 400)
            self.assertEquals(f(a), aqi_verbose(a))
        
    def test_1(self, f):
        lst1 = [1, 2, '3']
        lst1r = ['3', 2, 1]
        lst2 = ['a', 'b', [1,2,3], 5, [[6]], 7, 8, 9, 10]
        lst2r = [10, 9, 8, 7, [[6]], 5, [1, 2, 3], 'b', 'a']

        f(lst1)
        f(lst2)
        self.assertEquals(lst1r, lst1)
        self.assertEquals(lst2r, lst2)
        self.assertEquals(f(lst1), None)

    def test_2(self, f):
        for i in range(30):
            l = random.randint(0, 300)
            lst = []
            for _ in range(l):
                lst.append(random.randint(0, 300))
            self.assertAlmostEquals(f(lst), np.average(lst))


    def test_3(self, f):
        xs = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29]
        ps = [True,True,False,True,False,True,False,False,False,True,False,True,False,False,False,True,False,True,False,False,False,True,False,False,False,False,False,True]

        for i in range(len(xs)):
            self.assertEquals(f(xs[i]), ps[i])

    def test_4(self, f):
        x = 3
        y = 4
        z = 5
        
        self.assertEquals(f(3), 9)
        self.assertEquals(f(4), 16)
        self.assertEquals(f(5), 25)


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