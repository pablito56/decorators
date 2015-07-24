#! /usr/bin/env python
#-*- coding: utf-8 -*-
u"""
>>> import time
>>> from solution_mod_03 import factorial

>>> t1_start = time.time()
>>> res1 = factorial(200)
>>> t1_elapsed = time.time() - t1_start

>>> t2_start = time.time()
>>> res2 = factorial(200)
>>> t2_elapsed = time.time() - t2_start

>>> print "TIMES:", t1_elapsed, "vs.", t2_elapsed
TIMES: 20.1713969707 vs. 0.102944135666
"""

#===============================================================================
# EXERCISE: exercise_mod_03.py
#
# - Use memoization to speed up factorial computation
#     - http://en.wikipedia.org/wiki/Memoization
#     - Use our simple in-memory cache to store calls results (exercises.simcache)
#
# - Run the tests in 'tests_mod_03.py' executing 'nosetests -v' inside its folder
#
# - Check the solution in module 'solution_mod_03.py'
#===============================================================================


from time import sleep
from .. import simcache


def factorial(x):
    sleep(0.1)  # This sleep can not be removed!!
    if x < 2:
        return 1
    return x * factorial(x - 1)
