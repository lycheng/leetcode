# -*- coding: utf-8 -*-

__author__ = 'lycheng'
__email__ = "lycheng997@gmail.com"


import unittest

from matrix import search_2d_matrix


class TestMatrixSearch(unittest.TestCase):

    def test_search_2d_matrix_i(self):

        src = [
            [1,   3,  5,  7],
            [10, 11, 16, 20],
            [23, 30, 34, 50]
        ]
        so = search_2d_matrix.Solution()

        self.assertFalse(so.searchMatrix_i(src, 0))
        self.assertFalse(so.searchMatrix_i([], 3))
        self.assertFalse(so.searchMatrix_i(src, 51))
        self.assertTrue(so.searchMatrix_i(src, 3))
        self.assertTrue(so.searchMatrix_i(src, 11))

    def test_search_2d_matrix_ii(self):
        src = [
            [1,   4,  7, 11, 15],
            [2,   5,  8, 12, 19],
            [3,   6,  9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30]
        ]
        so = search_2d_matrix.Solution()
        self.assertFalse(so.searchMatrix_ii(src, 0))
        self.assertFalse(so.searchMatrix_ii(src, 20))
        self.assertFalse(so.searchMatrix_ii(src, 31))
        self.assertFalse(so.searchMatrix_ii([], 3))

        self.assertTrue(so.searchMatrix_ii(src, 5))
        self.assertTrue(so.searchMatrix_ii(src, 7))
        self.assertTrue(so.searchMatrix_ii(src, 8))

        self.assertFalse(so.searchMatrix_ii_submisson2([], 5))
        self.assertFalse(so.searchMatrix_ii_submisson2(src, 31))

        self.assertTrue(so.searchMatrix_ii_submisson2(src, 5))

        src = [[-1], [-1]]
        self.assertFalse(so.searchMatrix_ii_submisson2(src, -2))
