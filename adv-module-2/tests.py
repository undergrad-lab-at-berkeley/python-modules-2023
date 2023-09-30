import math
import random
import __main__
import datetime
import unittest
import numpy as np
from IPython.display import Markdown, display

pi = np.pi
g = 9.81

########## TESTS ##########
class Tests(unittest.TestCase):

    def test_accel2(self, get_accel_2):

        angles = np.array([-pi / 3, pi / 6])
        vels = np.array([pi / 12, -pi / 6])
        lengths = np.array([1, 2])
        masses = np.array([2, 1])
        result = get_accel_2(angles, vels, lengths, masses)
        self.assertTrue(np.allclose(result, np.array([ 8.67847966, -2.48676946])))
        self.assertTrue(type(result)==np.ndarray)
    
    def test_step(self, step):
        angles = np.array([23 * np.pi / 12, -np.pi / 6])
        vels = np.array([np.pi / 2, -np.pi / 12])
        accels = np.array([-0.1, 0.1])
        angles_new, vels_new = step(angles, vels, accels, dt=0.5)
        self.assertTrue(np.allclose(
            angles_new,
            np.array([0.49859878, 5.65368684]))
        )
        self.assertTrue(np.allclose(
            vels_new,
            np.array([ 1.52079633, -0.21179939])))

    def test_simulate(self, simulate):
        n_steps = 50
        dt = 1e-1
        angles = np.array([23 * np.pi / 12, -np.pi / 6])
        lengths = np.array([2, 3])
        masses = np.array([1, 4])
        times, pos = simulate(angles, lengths, masses, dt, n_steps)
        self.assertTrue(np.allclose(dt, np.diff(times)))
        sim_end_state = np.array([[-0.43249737, -1.95267663], [-1.53645013, -4.7421727]])
        self.assertTrue(np.allclose(
            pos[-1],
            sim_end_state))
        self.assertTrue(type(times)==np.ndarray)
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
