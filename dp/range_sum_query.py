# -*- coding: utf-8 -*-


class NumArray(object):
    ''' https://leetcode.com/problems/range-sum-query-immutable/
    '''

    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        len_nums = len(nums)
        self.sums = [0] * (len_nums+1)

        for i in range(0, len_nums):
            self.sums[i+1] = self.sums[i] + nums[i]

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sums[j+1] - self.sums[i]
