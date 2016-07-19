#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

__author__ = 'lycheng'
__email__ = "lycheng997@gmail.com"

TARGET = -1


def guess(num):
    if TARGET > num:
        return 1
    elif TARGET < num:
        return -1
    return 0


class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        j = n

        while i <= j:
            mid = (i + j) / 2

            r = guess(mid)

            if r == 0:
                return mid
            elif r < 0:
                j = mid - 1
            else:
                i = mid + 1
        return -1
