# def solution(A, K):
#     n = len(A)
#     for i in range(n - 1):
#         if not (0 <= A[i + 1] - A[i] <= 1):
#             return False
#     if (A[0] != 1 or A[n - 1] < K):
#         return False
#     else:
#         return True
#
#
# import unittest
#
# class Test(unittest.TestCase):
#
#     def test_1(self):
#         self.assertEqual(solution([1, 1, 2, 3, 3], 3), True)
#
#     def test_2(self):
#         self.assertEqual(solution([1, 1, 3], 2), False)
#
#     def test_3(self):
#         self.assertEqual(solution([1, 2, 3, 3], 4), False)
#
#     def test_4(self):
#         self.assertEqual(solution([1, 2, 3, 3], 2), True)
#
#     def test_5(self):
#         self.assertEqual(solution([1, 2, 3, 3], 2), True)
#
#     def test_6(self):
#         self.assertEqual(solution([1, 2, 3, 3, 5], 5), False)
#
#     def test_7(self):
#         self.assertEqual(solution([1, 2, 3, 3, 5], 4), False)
#
# def test_8(self):
#     self.assertEqual(solution([1, 2, 3, 3, 5], 3), True)

# def solution(A):
#     swaps = 0
#     i = 0
#     while i < len(A):
#         cur_sum, cur_swaps = 0, 0
#         new_A, j = list(A), 0
#             if cur_sum + new_A[i] < 0:
#                 A.append(A.pop(i))
#                 swaps += 1
#
#             else:
#                 cur_sum += A[i]
#                 i += 1
#
#     return swaps


import unittest


class Test(unittest.TestCase):

    def test_1(self):
        self.assertEqual(solution([10, -10, -1, -1, 10]), 1)

    def test_2(self):
        self.assertEqual(solution([-1, -1, -1, 1, 1, 1, 1]), 3)

    def test_3(self):
        self.assertEqual(solution([5, -2, -3, 1]), 0)