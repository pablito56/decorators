#! /usr/bin/env python
#-*- coding: utf-8 -*-
u"""
Module 04 (advanced decorators) exercise: apply memoization to factorial and fibonacci
"""

#===============================================================================
# EXERCISE: exercise_mod_04.py
#
# - Use memoization to speed up factorial and fibonacci computation
#     - Take care to not share the same cache for both
#     - Ideally it should be possible to specify different cache setup for each decorated function
#
# - Run the tests in 'tests_mod_04.py' executing 'nosetests -v' inside its folder
#
# - Check the solution in module 'solution_mod_04.py'
#===============================================================================


import functools
import time
from collections import OrderedDict


def factorial(n):
    """Return n!"""
    time.sleep(0.1)  # Do not remove it
    if n < 2:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    """Return the nth fibonacci number"""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
