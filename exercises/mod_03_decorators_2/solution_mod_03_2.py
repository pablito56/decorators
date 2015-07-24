#! /usr/bin/env python
#-*- coding: utf-8 -*-
u"""
MOD 03_2: Solution: Implement an exception catcher decorator.
"""

#===============================================================================
# EXERCISE: exercise_mod_03_2.py
#
# - Implement a decorator which catches exceptions and returns None
#
# - Run the tests in 'tests_mod_03_2.py' executing 'nosetests -v' inside its folder
#
# - Check the solution in module 'solution_mod_03_2.py'
#===============================================================================


import functools


def catcher_decorator(decorated_func):
    @functools.wraps(decorated_func)
    def wrapper(*args, **kwargs):  # TODO: Accept arbitrary positional and keyword args
        try:
            return decorated_func(*args, **kwargs)
        except Exception as e:
            print "GOT EXCEPTION", e
            return None
    return wrapper


@catcher_decorator
def dummy_function(*args, **kwargs):
    if isinstance(args[0], Exception):
        raise args[0]
    return args[0]
