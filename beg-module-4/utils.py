# A couple of math utility functions.

from math import sqrt
import requests
from io import BytesIO

def fibonacci(n):
	r"""
	Gets the 'n'th Fibonacci number, i.e. the number f_n satisfying the relationship f_n = f_{n-1} + f_{n-2} where f_1 = f_2 = 1.
	Parameters
	----------
	n : int
		The index of the Fibonacci number to get
	Returns
	-------
	fib : int
		The 'n'th Fibonacci number
	"""
	assert isinstance(n, int) and n >= 0, "only nonnegative integers are valid indices to the Fibonacci sequence."
	phi = (1 + sqrt(5)) / 2
	fib = (phi ** n  - (1 - phi) ** n) / sqrt(5)
	return round(fib)

def factorial(n):
	"""
	Gets n! or n factorial, which is defined as n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.
	Parameters
	----------
	n : int
		The number whose factorial we want.
	Returns
	-------
	fact : int
		The factorial of n.
	"""
	assert isinstance(n, int) and n >= 0, "only nonnegative integers have factorials."
	if n == 0:
		return 1
	return n * factorial(n - 1)


def get_planets():
	'''
	Archive of the planets csv can be found in this directory
	'''
	url = "http://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=q1_q16_koi&select=*"
	r = requests.get(url)
	return BytesIO(r.content)
