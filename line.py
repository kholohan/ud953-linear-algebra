# -*- coding: utf-8 -*-
# Author: github.com/kholohan

from decimal import Decimal, getcontext

from vector import Vector

getcontext().prec = 30


class Line(object):

    NO_NONZERO_ELTS_FOUND_MSG = 'No nonzero elements found'

    def __init__(self, normal_vector=None, constant_term=None):
        self.dimension = 2

        if not normal_vector:
            all_zeros = [0]*self.dimension
            normal_vector = Vector(all_zeros)
        self.normal_vector = normal_vector

        if not constant_term:
            constant_term = 0
        self.constant_term = constant_term

        self.set_basepoint()


    def set_basepoint(self):
        try:
            n = self.normal_vector
            c = self.constant_term
            basepoint_coords = [0]*self.dimension

            initial_index = Line.first_nonzero_index(n)
            initial_coefficient = n[initial_index]

            basepoint_coords[initial_index] = c / initial_coefficient
            self.basepoint = Vector(basepoint_coords)

        except Exception as e:
            if str(e) == Line.NO_NONZERO_ELTS_FOUND_MSG:
                self.basepoint = None
            else:
                raise e

    def __eq__(self, line):
        basepoint_diff = self.basepoint - line.basepoint
        return basepoint_diff.is_orthogonal(self.normal_vector)

    def __str__(self):

        num_decimal_places = 3

        def write_coefficient(coefficient, is_initial_term=False):
            coefficient = round(coefficient, num_decimal_places)
            if coefficient % 1 == 0:
                coefficient = int(coefficient)

            output = ''

            if coefficient < 0:
                output += '-'
            if coefficient > 0 and not is_initial_term:
                output += '+'

            if not is_initial_term:
                output += ' '

            if abs(coefficient) != 1:
                output += '{}'.format(abs(coefficient))

            return output

        n = self.normal_vector

        try:
            initial_index = Line.first_nonzero_index(n)
            terms = [write_coefficient(n[i], is_initial_term=(i==initial_index)) + 'x_{}'.format(i+1)
                     for i in range(self.dimension) if round(n[i], num_decimal_places) != 0]
            output = ' '.join(terms)

        except Exception as e:
            if str(e) == self.NO_NONZERO_ELTS_FOUND_MSG:
                output = '0'
            else:
                raise e

        constant = round(self.constant_term, num_decimal_places)
        if constant % 1 == 0:
            constant = int(constant)
        output += ' = {}'.format(constant)

        return output

    def is_equal(self, line):
        return self.__eq__(line)

    def intersection(self, line, tolerance=1e-10):
        if self == line : return self.normal_vector #Lines are the same
        elif self.is_parallel(line) : return None

        denominator = (self.normal_vector[0] * line.normal_vector[1]) - (self.normal_vector[1] * line.normal_vector[0]) #AD-BC (constants of both lines)
        x = ((line.normal_vector[1] * self.constant_term) - (self.normal_vector[1] * line.constant_term)) / denominator # (Dk_1 - Bk_2) / (AD - BC)
        y = ((self.normal_vector[0] * line.constant_term) - (line.normal_vector[0] * self.constant_term)) / denominator # (Ak_2 + Ck_1) / (AD - BC)

        return Vector([x, y])

    def is_orthogonal(self, line):
        return self.normal_vector.is_orthogonal(line.normal_vectorm)

    def is_parallel(self, line):
        return self.normal_vector.is_parallel(line.normal_vector)



    @staticmethod
    def first_nonzero_index(iterable):
        for k, item in enumerate(iterable):
            if not MyDecimal(item).is_near_zero():
                return k
        raise Exception(Line.NO_NONZERO_ELTS_FOUND_MSG)


class MyDecimal(Decimal):
    def is_near_zero(self, eps=1e-10):
        return abs(self) < eps