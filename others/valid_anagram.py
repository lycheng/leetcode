#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

__author__ = 'lycheng'
__email__ = "lycheng997@gmail.com"


class Solution(object):
    ''' https://leetcode.com/problems/valid-anagram/
    '''

    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str

        :rtype: bool
        """
        if len(s) != len(t):
            return False

        char_count = {}
        for c in s:
            if c not in char_count:
                char_count[c] = 0
            char_count[c] += 1

        for c in t:
            if not char_count.get(c):
                return False
            char_count[c] -= 1

        return True
