# -*- coding: utf-8 -*-


class Solution(object):
    ''' https://leetcode.com/problems/coin-change/
    '''
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        count = [0] + [-1] * amount
        for x in range(amount):
            if count[x] < 0:
                continue
            for c in coins:
                if x + c > amount:
                    continue
                if count[x + c] < 0 or count[x + c] > count[x] + 1:
                    count[x + c] = count[x] + 1
        return count[amount]

    def coinChangeTLE(self, coins, amount):
        if amount == 0:
            return 0

        min_coin_count = dict()
        for coin in coins:
            min_coin_count[coin] = 1

        for i in range(1, amount+1):
            if i in min_coin_count:
                continue

            min_count = amount
            updated = False
            for coin in coins:
                if (i - coin) not in min_coin_count:
                    continue

                if min_coin_count[i - coin] + 1 < min_count:
                    min_count = min_coin_count[i - coin] + 1
                    updated = True

            if updated:
                min_coin_count[i] = min_count

        print min_coin_count

        if amount in min_coin_count:
            return min_coin_count[amount]
        return -1
