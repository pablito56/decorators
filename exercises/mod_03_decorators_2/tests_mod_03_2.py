#! /usr/bin/env python
#-*- coding: utf-8 -*-
u"""
MOD 03_2: Test: Implement an exception catcher decorator.
"""

import unittest
from exercise_mod_03_2 import dummy_function
# from solution_mod_03_2 import dummy_function


class TestCatcher(unittest.TestCase):
    def test_catching(self):
        """Test that catches an exception
        """
        self.assertIsNone(dummy_function(SystemError()))

    def test_no_exception(self):
        """Test that catches an exception
        """
        inputs = 7, 8, 9
        self.assertEquals(dummy_function(*inputs, name="Hello"), inputs[0])


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
