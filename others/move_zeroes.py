#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/move-zeroes/
'''

__author__ = 'lycheng'
__email__ = "lycheng997@gmail.com"


class Solution(object):

    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        len_nums = len(nums)
        if len_nums <= 1:
            return

        i = 0
        lidx = 1
        while lidx < len_nums:
            if nums[i]:
                i += 1
                lidx = i + 1 if i >= lidx else lidx
                continue

            if not nums[lidx]:
                lidx += 1
                continue
            nums[lidx], nums[i] = nums[i], nums[lidx]
