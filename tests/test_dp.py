# -*- coding: utf-8 -*-

import unittest
from random import shuffle

from dp import range_sum_query
from dp import range_sum_query_2d
from dp import max_profit


class TestDp(unittest.TestCase):

    def test_range_sum_query(self):
        '''
        '''
        obj = range_sum_query.NumArray(range(10))
        self.assertEqual(obj.sumRange(0, 9), sum(range(10)))

        obj = range_sum_query.NumArray([-2, 0, 3, -5, 2, -1])
        self.assertEqual(obj.sumRange(0, 2), 1)
        self.assertEqual(obj.sumRange(2, 5), -1)
        self.assertEqual(obj.sumRange(0, 5), -3)

    def test_range_sum_query_2d(self):
        '''
        '''
        matrix = [
            [3, 0, 1, 4, 2],
            [5, 6, 3, 2, 1],
            [1, 2, 0, 1, 5],
            [4, 1, 0, 1, 7],
            [1, 0, 3, 0, 5]
        ]
        obj = range_sum_query_2d.NumMatrix(matrix)
        self.assertEqual(obj.sumRegion(1, 1, 2, 2), 11)
        self.assertEqual(obj.sumRegion(2, 1, 4, 3), 8)
        self.assertEqual(obj.sumRegion(1, 2, 2, 4), 12)

        obj = range_sum_query_2d.NumMatrix([])
        self.assertEqual(obj.sumRegion(1, 1, 2, 2), 0)

    def test_max_profit(self):
        '''
        '''
        prices = range(1, 10)
        so = max_profit.Solution()

        self.assertEqual(0, so.maxProfit_I([]))
        shuffle(prices)
        self.assertEqual(8, so.maxProfit_I(prices))

        self.assertEqual(0, so.maxProfit_II([1]))
        prices = range(1, 10)
        self.assertEqual(8, so.maxProfit_II(prices))
