# -*- coding: utf-8 -*-

__author__ = 'lycheng'
__email__ = "lycheng997@gmail.com"


class Solution(object):
    ''' https://leetcode.com/problems/nim-game/
    '''

    def canWinNim_out_of_memory(self, n):
        """
        :type n: int
        :rtype: bool
        """
        win_stones = set([1, 2, 3])

        if n in win_stones:
            return True

        for i in range(4, n+1):

            # all failed
            if all([i - pick_stones in win_stones
                    for pick_stones in range(1, 4)]):
                continue
            win_stones.add(i)
        return n in win_stones

    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return bool(n % 4)
