#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

__author__ = 'lycheng'
__email__ = "lycheng997@gmail.com"

from public import TreeNode

class Solution(object):
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        if not triangle:
            return 0

        for row in range(len(triangle) - 2, -1, -1):
            len_trigle_row = len(triangle[row])
            for column in range(0, len_trigle_row):
                cur_min_sum = min(triangle[row][column] + triangle[row+1][column],
                        triangle[row][column] + triangle[row+1][column+1])
                triangle[row][column] = cur_min_sum

        return triangle[0][0]

    def test_minimumTotal(self):
        src = [
                [2],
                [3,4],
                [6,5,7],
                [4,1,8,3]
        ]
        print self.minimumTotal(src)

    def hasPathSum(self, root, sum):
        if not root:
            return False

        need_sum = sum - root.val
        if need_sum == 0 and not root.left and not root.right:
            return True

        result = False
        if root.left:
            result = self.hasPathSum(root.left, need_sum)

        if root.right:
            result = result or self.hasPathSum(root.right, need_sum)

        return result

    def test_hasPathSum(self):

        root = TreeNode(5)
        root.left = TreeNode(4)
        root.left.left = TreeNode(11)
        root.left.left.left = TreeNode(7)
        root.left.left.right = TreeNode(2)
        root.right = TreeNode(8)
        root.right.left = TreeNode(13)
        root.right.right = TreeNode(4)
        root.right.right.right = TreeNode(1)

        print self.hasPathSum(root, 22)


if __name__ == "__main__":
    so = Solution()
    # so.test_minimumTotal()
    so.test_hasPathSum()
