# -*- coding: utf-8 -*-
# Author: github.com/kholohan

import unittest

from vector import Vector
from line import Line

class LineTest(unittest.TestCase):

    def test_is_equal(self):
        # line 1: 4.046x + 2.836y = 1.21
        # line 2: 10.115x + 7.09y = 3.025
        line1 = Line(Vector([4.046, 2.836]), 1.21)
        line2 = Line(Vector([10.115, 7.09]), 3.025)

        result = line1 == line2
        self.assertTrue(result)

    def test_is_equal2(self):
        # line 1: 7.204x + 3.182y = 8.68
        # line 2: 8.172x + 4.114y = 9.883
        line1 = Line(Vector([7.204, 3.182]), 8.68)
        line2 = Line(Vector([8.172, 4.114]), 9.883)

        result = line1 == line2
        self.assertFalse(result)

    def test_is_equal3(self):
        # line 1: 1.182x + 5.562y = 6.744
        # line 2: 1.773x + 8.343y = 9.525
        line1 = Line(Vector([1.182, 5.562]), 6.744)
        line2 = Line(Vector([1.773, 8.343]), 9.525)

        result = line1 == line2
        self.assertFalse(result)

    def test_is_parallel1(self):
        # line 1: 4.046x + 2.836y = 1.21
        # line 2: 10.115x + 7.09y = 3.025
        line1 = Line(Vector([4.046, 2.836]), 1.21)
        line2 = Line(Vector([10.115, 7.09]), 3.025)

        result = line1.is_parallel(line2)
        self.assertTrue(result)

    def test_is_parallel2(self):
        # line 1: 7.204x + 3.182y = 8.68
        # line 2: 8.172x + 4.114y = 9.883
        line1 = Line(Vector([7.204, 3.182]), 8.68)
        line2 = Line(Vector([8.172, 4.114]), 9.883)

        result = line1.is_parallel(line2)
        self.assertFalse(result)

    def test_is_parallel3(self):
        # line 1: 1.182x + 5.562y = 6.744
        # line 2: 1.773x + 8.343y = 9.525
        line1 = Line(Vector([1.182, 5.562]), 6.744)
        line2 = Line(Vector([1.773, 8.343]), 9.525)

        result = line1.is_parallel(line2)
        self.assertTrue(result)

    def test_intersection(self):
        # line 1: 4.046x + 2.836y = 1.21
        # line 2: 10.115x + 7.09y = 3.025
        line1 = Line(Vector([4.046, 2.836]), 1.21)
        line2 = Line(Vector([10.115, 7.09]), 3.025)

        result = line1.intersection(line2)
        self.assertEquals(result, line1.normal_vector)


    def test_intersection2(self):
        # line 1: 7.204x + 3.182y = 8.68
        # line 2: 8.172x + 4.114y = 9.883
        line1 = Line(Vector([7.204, 3.182]), 8.68)
        line2 = Line(Vector([8.172, 4.114]), 9.883)

        result = line1.intersection(line2)
        answer = Vector([1.1727766354646414, 0.07269551166333184])
        self.assertEquals(result, answer)


    def test_intersection3(self):
        # line 1: 1.182x + 5.562y = 6.744
        # line 2: 1.773x + 8.343y = 9.525
        line1 = Line(Vector([1.182, 5.562]), 6.744)
        line2 = Line(Vector([1.773, 8.343]), 9.525)

        result = line1.intersection(line2)
        self.assertFalse(result)


    def test_equals(self):
        # line 1: 4.046x + 2.836y = 1.21
        # line 2: 10.115x + 7.09y = 3.025
        line1 = Line(Vector([4.046, 2.836]), 1.21)
        line2 = Line(Vector([10.115, 7.09]), 3.025)

        result = line1 == line2
        self.assertTrue(result)

    def test_equals2(self):
        # line 1: 7.204x + 3.182y = 8.68
        # line 2: 8.172x + 4.114y = 9.883
        line1 = Line(Vector([7.204, 3.182]), 8.68)
        line2 = Line(Vector([8.172, 4.114]), 9.883)

        result = line1 == line2
        self.assertFalse(result)

    def test_equals3(self):
        # line 1: 1.182x + 5.562y = 6.744
        # line 2: 1.773x + 8.343y = 9.525
        line1 = Line(Vector([1.182, 5.562]), 6.744)
        line2 = Line(Vector([1.773, 8.343]), 9.525)

        result = line1 == line2
        self.assertFalse(result)