# -*- coding: utf-8 -*-

import unittest

from dp import range_sum_query
from dp import range_sum_query_2d
from dp import max_profit
from dp import house_robber
from dp import climbing_stairs
from dp import coin_change


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
        prices = [2, 1, 3, 0]
        self.assertEqual(2, so.maxProfit_I(prices))

        self.assertEqual(0, so.maxProfit_II([1]))
        prices = range(1, 10)
        self.assertEqual(8, so.maxProfit_II(prices))

    def test_rob(self):
        '''
        '''
        so = house_robber.Solution()
        self.assertEqual(0, so.rob([]))

        self.assertEqual(2, so.rob([1, 2]))

        self.assertEqual(9, so.rob([1, 2, 3, 4, 5]))

        self.assertEqual(5, so.rob([1, 5, 3]))

    def test_climbStairs(self):
        '''
        '''
        so = climbing_stairs.Solution()
        self.assertEqual(2, so.climbStairs(2))
        self.assertEqual(3, so.climbStairs(3))

    def test_coin_change(self):
        so = coin_change.Solution()
        self.assertEqual(so.coinChange([1, 2, 5], 11), 3)
        self.assertEqual(so.coinChangeTLE([1, 2, 5], 11), 3)

        self.assertEqual(so.coinChange([2], 3), -1)
        self.assertEqual(so.coinChangeTLE([2], 3), -1)
        self.assertEqual(so.coinChange([1], 0), 0)
        self.assertEqual(so.coinChangeTLE([1], 0), 0)
        self.assertEqual(so.coinChange(
            [370, 417, 408, 156, 143, 434, 168, 83, 177, 280, 117],
            9953),
            24)
        self.assertEqual(so.coinChangeTLE(
            [370, 417, 408, 156, 143, 434, 168, 83, 177, 280, 117],
            9953),
            24)
