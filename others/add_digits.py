# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/add-digits/
'''


class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if not num:
            return 0

        result = num % 9
        if not result:
            result = 9
        return result
