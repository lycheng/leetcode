# -*- coding: utf-8 -*-


class Solution(object):
    '''
    '''

    def maxProfit_I(self, prices):
        if not prices:
            return 0
        lowest = prices[0]
        max_profit = 0

        for price in prices:
            diff = price - lowest
            if max_profit < diff:
                max_profit = diff

            if price < lowest:
                lowest = price

        return max_profit

    def maxProfit_II(self, prices):
        if not prices or len(prices) == 1:
            return 0

        max_profit = 0
        for day in range(1, len(prices)):
            diff = prices[day] - prices[day-1]
            if diff > 0:
                max_profit += diff

        return max_profit
