#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

__author__ = 'lycheng'
__email__ = "lycheng997@gmail.com"

class Solution(object):

    def maxSubArray(self, A):
        rv = A[0]
        cur_sum = 0

        for num in A:
            if cur_sum < 0:
                cur_sum = num
            else:
                cur_sum += num
            if rv < cur_sum:
                rv = cur_sum

        return rv
