import sourcedefender
from okEncode import okEncode
import os
import math
import unittest
import compute
import numpy as np
pi = np.pi

class ComputeTests(unittest.TestCase):
    def test_pos(self):
        lengths = [1, 3, 4]
        thetas = [pi / 4, -pi / 3, pi / 6]
        assert np.allclose(
            compute.positions(thetas, lengths),
            np.array([[ 0.70710678, -0.70710678],
                      [-1.89096943, -2.20710678],
                      [ 0.10903057, -5.6712084 ]])
        )

    def test_accel1(self):
        angle = -pi / 3
        vel = pi / 12
        length = 1
        m = 1
        assert np.isclose(compute.get_accel_1(angle, vel, length, m), 8.495709)

    def test_accel2(self):
        angles = np.array([-pi / 3, pi / 6])
        vels = np.array([pi / 12, -pi / 6])
        lengths = np.array([1, 2])
        masses = np.array([2, 1])
        assert np.allclose(
            compute.get_accel_2(angles, vels, lengths, masses),
            np.array([ 8.67847966, -2.48676946])
        )

    def test_step(self):
        angles = np.array([23 * np.pi / 12, -np.pi / 6])
        vels = np.array([np.pi / 2, -np.pi / 12])
        accels = np.array([-0.1, 0.1])
        angles_new, vels_new = compute.step(angles, vels, accels, dt=0.5, noisy=False)
        assert np.allclose(
            angles_new,
            np.array([0.49859878, 5.65368684])
        )
        assert np.allclose(
            vels_new,
            np.array([ 1.52079633, -0.21179939])
        )

    def test_simulate(self):
        n_steps = 50
        dt = 1e-1
        angles = np.array([23 * np.pi / 12, -np.pi / 6])
        lengths = np.array([2, 3])
        masses = np.array([1, 4])
        times, pos = compute.simulate(angles, lengths, masses, dt, n_steps, noisy=False)
        assert np.allclose(dt, np.diff(times))
        sim_end_state = np.array([[-0.43249737, -1.95267663], [-1.53645013, -4.7421727]])
        assert np.allclose(
            pos[-1], 
            sim_end_state
        )

def run_tests():
    results = []
    test_names = ["test_pos", "test_accel1", "test_accel2", "test_step", "test_simulate"]
    for name in test_names:
        test = eval("ComputeTests." + name)
        try:
            test(ComputeTests())
            results.append(True)
        except BaseException:
            results.append(False)
    return results

# wrapper function
def generate_token(CAL_ID):
    module_name = 'pythonModule4'
    num_questions = 5
    id = CAL_ID
    ok = okEncode(module_name, id, num_questions)

    results = run_tests()
    for i in range(len(results)):
        if results[i]:
            ok.correct(i)
        else:
            ok.incorrect(i)
            
    ok.generate_token()