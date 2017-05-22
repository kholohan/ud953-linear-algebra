# -*- coding: utf-8 -*-
# Author: github.com/kholohan

import unittest

from vector import Vector
from plane import Plane

class PlaneTest(unittest.TestCase):

    def test_is_equal(self):
        # plane 1: -0.412x + 3.806y + 0.728z = -3.46
        # plane 2: 1.03x + 9.515y - 1.82z = 8.65
        plane1 = Plane(Vector([-0.412, 3.806, 0.728]), -3.46)
        plane2 = Plane(Vector([1.03, 9.515, -1.82]), 8.65)

        result = plane1 == plane2
        self.assertTrue(result)

    def test_is_equal2(self):
        # plane 1: 2.611x + 5.528y + 0.283z = 4.6
        # plane 2: 7.715x + 8.306y + 5.342z = 3.76
        plane1 = Plane(Vector([2.611, 5.528, 0.283]), 4.6)
        plane2 = Plane(Vector([7.715, 8.306, 5.342]), 3.76)

        result = plane1 == plane2
        self.assertFalse(result)

    def test_is_equal3(self):
        # plane 1: -7.926x + 8.625y - 7.217 z = -7.952
        # plane 2: -2.642x + 2.875y - 2.404z = -2.443
        plane1 = Plane(Vector([-7.926, 8.625, -7.217]), -7.952)
        plane2 = Plane(Vector([-2.642, 2.875, -2.404]), -2.443)

        result = plane1 == plane2
        self.assertFalse(result)

    def test_is_parallel(self):
        # plane 1: -0.412x + 3.806y + 0.728z = -3.46
        # plane 2: 1.03x + 9.515y - 1.82z = 8.65
        plane1 = Plane(Vector([-0.412, 3.806, 0.728]), -3.46)
        plane2 = Plane(Vector([1.03, 9.515, -1.82]), 8.65)

        result = plane1.is_parallel(plane2)
        self.assertFalse(result)

    def test_is_parallel2(self):
        # plane 1: 2.611x + 5.528y + 0.283z = 4.6
        # plane 2: 7.715x + 8.306y + 5.342z = 3.76
        plane1 = Plane(Vector([2.611, 5.528, 0.283]), 4.6)
        plane2 = Plane(Vector([7.715, 8.306, 5.342]), 3.76)

        result = plane1.is_parallel(plane2)
        self.assertFalse(result)

    def test_is_parallel3(self):
        # plane 1: -7.926x + 8.625y - 7.217 z = -7.952
        # plane 2: -2.642x + 2.875y - 2.404z = -2.443
        plane1 = Plane(Vector([-7.926, 8.625, -7.212]), -7.952)
        plane2 = Plane(Vector([-2.642, 2.875, -2.404]), -2.443)

        result = plane1.is_parallel(plane2)
        self.assertTrue(result)