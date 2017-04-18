# -*- coding: utf-8 -*-
# Author: github.com/kholohan

from math import acos, degrees, sqrt, pi

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def __add__(self, v):
        return Vector([x+y for x, y in zip(self.coordinates, v.coordinates)])

    def __sub__(self, v):
        return Vector([x-y for x, y in zip(self.coordinates, v.coordinates)])

    def __mul__(self, v):
        if isinstance(v, Vector):
            return Vector([x*y for x, y in zip(self.coordinates, v.coordinates)])
        else:
            return Vector([x*v for x in self.coordinates])

    def angle_degree(self, v):
        return degrees(self.angle_radian(v))

    def angle_radian(self, v):
        return acos(round(self.dot_product(v) / (self.magnitude() * v.magnitude()), 3))

    def dot_product(self, v):
        if isinstance(v, Vector):
            return sum([x*y for x, y in zip(self.coordinates, v.coordinates)])

    def is_orthogonal(self, v, tolerance=1e-10):
        return abs(self.dot_product(v)) < tolerance

    def is_parallel(self, v, tolerance=1e-10):
        if self.is_zero() or v.is_zero(): return True
        else:
            items = [x / y for x, y in zip(self.coordinates, v.coordinates)]
            return all([abs(items[0] - item) < 1e-10 for item in items])

    def is_zero(self, tolerance=1e-10):
        return self.magnitude() < tolerance

    def magnitude(self):
        return sqrt(sum([x**2 for x in self.coordinates]))

    def normalize(self):
        try:
            return Vector([(1 / self.magnitude()) * x for x in self.coordinates])
        except ZeroDivisionError:
            raise Exception('Cannot normalize the zero vector')

    # perpendicular, where v is base vector
    def orthogonal(self, base_vector):
            return self - self.projection(base_vector)

    #project self onto base vector v, parallel
    def projection(self, base_vector):
        return self.dot_product(base_vector.normalize()) * base_vector.normalize()

    def scalar_multiplication(self, v):
        return self.__mul__(v)



    __rmul__ = __mul__

