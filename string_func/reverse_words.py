# -*- coding: utf-8 -*-

__author__ = 'lycheng'
__email__ = "lycheng997@gmail.com"


class Solution(object):
    ''' https://leetcode.com/problems/reverse-words-in-a-string/
    '''

    def reverseWords(self, s):
        ''' reverseWords
        @param s, a string
        @return a string
        '''
        s = ' '.join(s.split())
        words = s.split(' ')
        words = [word[::-1] for word in words]
        return " ".join(words)[::-1]
