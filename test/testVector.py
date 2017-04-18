# -*- coding: utf-8 -*-
# Author: github.com/kholohan

import unittest

from vector import Vector

class VectorTest(unittest.TestCase):

    def test_vector_addition(self):
        v = Vector([8.218, -9.341])
        w = Vector([-1.129, 2.111])

        result = v + w

        answerVector = Vector([7.089, -7.229999999999999])
        self.assertEqual(result, answerVector)

    def test_vector_subtraction(self):
        v = Vector([7.119, 8.215])
        w = Vector([-8.223, 0.878])

        result = v - w

        answer_vector = Vector([15.342, 7.337])
        self.assertEqual(result, answer_vector)

    def test_vector_scalar_multiplication(self):
        v = Vector([1.671, -1.012, -0.318])

        result = v.scalar_multiplication(7.41)

        answer_vector = Vector([12.38211, -7.49892, -2.35638])
        self.assertEqual(result, answer_vector)

    def testMagnitude(self):
        v = Vector([-0.221, 7.437])

        result = v.magnitude()

        answer = 7.440282924728065
        self.assertEqual(result, answer)

    def testMagnitude2(self):
        v = Vector([8.813, -1.331, -6.247])

        result = v.magnitude()

        answer = 10.884187567292289
        self.assertEqual(result, answer)

    def test_normalize(self):
        v = Vector([5.581, -2.136])

        result = v.normalize()

        answer_vector = Vector([0.9339352140866403, -0.35744232526233])
        self.assertEqual(result, answer_vector)

    def test_normalize2(self):
        v = Vector([1.996, 3.108, -4.554])

        result = v.normalize()

        answer_vector = Vector([0.3404012959433014, 0.5300437012984873, -0.7766470449528029])
        self.assertEqual(result, answer_vector)


    def test_dot_product(self):
        v = Vector([7.887, 4.138])
        w = Vector([-8.802, 6.776])

        result = v.dot_product(w)
        answer = -41.382286
        self.assertEqual(result, answer)

    def test_dot_product2(self):
        v = Vector([-5.955, -4.904, -1.874])
        w = Vector([-4.496, -8.755, 7.103])

        result = v.dot_product(w)
        answer =  56.397178000000004
        self.assertEqual(result, answer)

    def test_angle_degree(self):
        v = Vector([7.35, 0.221, 5.188])
        w = Vector([2.751, 8.259, 3.985])

        result = v.angle_degree(w)
        answer = 60.26428689244719
        self.assertEqual(result, answer)

    def test_angle_radian(self):
        v = Vector([3.183, -7.627])
        w = Vector([-2.668, 5.319])

        result = v.angle_radian(w)
        answer =  3.07833655471465
        self.assertEqual(result, answer)

    def test_not_orthogonal(self):
        v = Vector([-7.579, -7.88])
        w = Vector([22.737, 23.64])

        result = v.is_orthogonal(w)
        self.assertFalse(result)

    def test_parallel(self):
        v = Vector([-7.579, -7.88])
        w = Vector([22.737, 23.64])

        result = v.is_parallel(w)
        self.assertTrue(result)

    def test_not_orthogonal2(self):
        v = Vector([-2.029, 9.97, 4.172])
        w = Vector([-9.231, -6.639, -7.245])

        result = v.is_orthogonal(w)
        self.assertFalse(result)

    def test_not_parallel(self):
        v = Vector([-2.029, 9.97, 4.172])
        w = Vector([-9.231, -6.639, -7.245])

        result = v.is_parallel(w)
        self.assertFalse(result)

    def test_orthogonal(self):
        v = Vector([-2.328, -7.284, -1.214])
        w = Vector([-1.821, 1.072, -2.94])

        result = v.is_orthogonal(w)
        self.assertTrue(result)

    def test_not_parallel2(self):
        v = Vector([-2.328, -7.284, -1.214])
        w = Vector([-1.821, 1.072, -2.94])

        result = v.is_parallel(w)
        self.assertFalse(result)

    def test_orthogonal2(self):
        v = Vector([2.118, 4.827])
        w = Vector([0, 0])

        result = v.is_orthogonal(w)
        self.assertTrue(result)

    def test_parallel4(self):
        v = Vector([2.118, 4.827])
        w = Vector([0, 0])

        result = v.is_parallel(w)
        self.assertTrue(result)

    def test_projection(self):
        v = Vector([3.039, 1.879])
        base_vector = Vector([0.825, 2.036])

        result = v.projection(base_vector)
        answer = Vector([1.082606962484467, 2.671742758325303])
        self.assertEquals(result, answer)


    def test_orthogonal(self):
        v = Vector([-9.88, -3.264, -8.159])
        base_vector = Vector([-2.155, -9.353, -9.473])

        result = v.orthogonal(base_vector)
        answer = Vector([-8.350081043195763, 3.376061254287722, -1.4337460427811841])
        self.assertEquals(result, answer)

    def test_find_orthogonal_parallel(self):
        v = Vector([3.009, -6.172, 3.692, -2.51])
        base_vector = Vector([6.404, -9.144, 2.759, 8.718])

        parallel_result = v.projection(base_vector)  #projection onto b
        orthogonal_result = v.orthogonal(base_vector)

        # v = parallel + orthonal
        v_reconstructed = parallel_result + orthogonal_result
        self.assertTrue(v.is_parallel(v_reconstructed))

if __name__ == '__main__':
    unittest.main()
