#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

__author__ = 'lycheng'
__email__ = "lycheng997@gmail.com"

from public import TreeNode

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

    def jump(self, A):
        if not A or len(A) == 1:
            return 0
        min_jump = 0
        beg = 0
        end = 0

        while end < len(A):
            min_jump += 1
            cur_can_jump_max = 0
            for index in range(beg, end+1):
                can_jump = A[index] + index
                if can_jump >= len(A) - 1:
                    return min_jump
                if can_jump> cur_can_jump_max:
                    cur_can_jump_max = can_jump

            beg = end + 1
            end = cur_can_jump_max
            index = index + 1

        return min_jump

    def permuteUnique(self, num):
        length = len(num)
        if length == 0:
            return []
        if length == 1:
            return [num]

        result = []
        pre_num = None
        num.sort()
        for i in range(length):
            if num[i] == pre_num:
                continue
            pre_num = num[i]
            for r in self.permuteUnique(num[0:i] + num[i+1:]):
                result.append([num[i]] + r)

        return result

    def numTrees(self, n):
        count = [0] * (n+1)
        count[0] = 1
        count[1] = 1
        for i in range(2, n+1):
            for j in range(0, i):
                count[i] += count[j] * count[i-j-1]

        return count[n]

    def uniquePaths(self, m, n):
        table = [[0] * m] * n
        for i in xrange(n):
            for j in xrange(m):
                if not i or not j:
                    table[i][j] = 1
                    continue
                table[i][j] = table[i-1][j] + table[i][j-1]

        return table[-1][-1]

    def sortedArrayToBST(self, num):
        if not num:
            return None

        mid = len(num) / 2
        root = TreeNode(num[mid])
        root.left = self.sortedArrayToBST(num[0:mid])
        root.right = self.sortedArrayToBST(num[mid+1:])
        return root


if __name__ == "__main__":
    so = Solution()
    # so.test_minimumTotal()
    # so.test_hasPathSum()
    # so.test_sumNumbers()
    # so.test_restoreIpAddresses()
    # print so.solveNQueens(4)
    # so.test_canJump()
    # print so.jump([2,3,1,1,4])
    # print so.permuteUnique([1,1,2])
    # print so.numTrees(3)
    # print so.uniquePaths(2, 3)
    print so.sortedArrayToBST([1, 2, 3])
