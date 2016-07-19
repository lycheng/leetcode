#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

__author__ = 'lycheng'
__email__ = "lycheng997@gmail.com"


class Solution(object):

    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        count = 0
        while i <= n:
            if i & n > 0:
                count += 1
            i = i << 1

        return count
