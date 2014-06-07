#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

__author__ = 'lycheng'
__email__ = "lycheng997@gmail.com"


class Solution(object):

    def canJump(self, A):

        max_len = 0
        len_of_A = len(A)
        i = 0

        while i <= max_len and i < len_of_A:
            if A[i] + i >= max_len:
                max_len = A[i] + i
            if max_len >= len_of_A - 1:
                return True
            i += 1
        return False


    def test_canJump(self):
        li = [2,3,1,1,4]
        # li = range(25000, 0, -1)
        print self.canJump(li)
        print self.canJump([3,2,1,0,4])


if __name__ == "__main__":
    so = Solution()
    # so.test_minimumTotal()
    # so.test_hasPathSum()
    # so.test_sumNumbers()
    # so.test_restoreIpAddresses()
    # print so.solveNQueens(4)
    so.test_canJump()

