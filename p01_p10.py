#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

__author__ = 'lycheng'
__email__ = "lycheng997@gmail.com"

class Solution(object):
    def reverseWords(self, s):
        ''' reverseWords
        @param s, a string
        @return a string
        '''
        s = ' '.join(s.split())  # 分割出一个个单词出来
        words = s.split(' ')
        words = [word[::-1] for word in words]
        return " ".join(words)[::-1]

    def singleNumber(self, li):
        ''' return the single num in array
        @param A, a list of integer
        @return an integer
        '''
        rv = reduce(lambda x, y: x ^ y, li)
        return rv



def run():
    o = Solution()
    # print o.reverseWords("    the sky is       blue")
    print o.singleNumber([1, 2, 3, 4, 5, 3, 2, 1, 4])


if __name__ == "__main__":
    run()
