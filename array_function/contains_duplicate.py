#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

__author__ = 'lycheng'
__email__ = "lycheng997@gmail.com"


class Solution(object):

    def containsDuplicate(self, nums):
        """ https://leetcode.com/problems/contains-duplicate/
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        _set = set(nums)
        return len(_set) != len(nums)

    def containsDuplicate_ii(self, nums, k):
        """ https://leetcode.com/problems/contains-duplicate-ii/
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False

        num_idx = {}

        for idx, num in enumerate(nums):
            if num not in num_idx:
                num_idx[num] = idx
                continue

            if idx - num_idx[num] <= k:
                return True

            num_idx[num] = idx
        return False
