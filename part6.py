#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

__author__ = 'lycheng'
__email__ = "lycheng997@gmail.com"

from public import TreeNode

import unittest

class Solution(unittest.TestCase):

    def pathSum(self, root, sum):

        self.result = []
        def helper(root, target, rv):
            if not root:
                return []

            next_target = target - root.val
            cur_rv = rv[:]
            cur_rv.append(root.val)
            if next_target == 0 and not root.left and not root.right:
                self.result.append(cur_rv)
                return

            if root.left:
                helper(root.left, next_target, cur_rv[:])
            if root.right:
                helper(root.right, next_target, cur_rv[:])

        helper(root, sum, [])
        return self.result

    def test_pathSum(self):
        root = TreeNode(5)
        root.left = TreeNode(4)
        root.right = TreeNode(8)
        root.left.left = TreeNode(11)
        root.left.left.left = TreeNode(7)
        root.left.left.right = TreeNode(2)
        root.right.left = TreeNode(13)
        root.right.right = TreeNode(4)
        root.right.right.left = TreeNode(5)
        root.right.right.right = TreeNode(1)

        self.assertEqual(self.pathSum(root, 22), [[5, 4, 11, 2], [5, 8, 4, 5]])

    def removeDuplicates(self, A):

        length = len(A)

        if length <= 1:
            return length

        index = 0
        for front in range(1, length):
            if A[index] != A[front]:
                index += 1
                A[index] = A[front]

        return index + 1

    def minPathSum(self, grid):
        row_num = len(grid)
        col_num = len(grid[0])

        table = []
        for row in range(row_num):
            table.append([0] * (col_num))

        for row_index in range(row_num):
            for col_index in range(col_num):
                if not row_index and not col_index:
                    table[0][0] = grid[0][0]
                    continue
                if not row_index:
                    min_prev = table[0][col_index-1]
                elif not col_index:
                    min_prev = table[row_index-1][0]
                else:
                    min_prev = min(table[row_index-1][col_index], table[row_index][col_index-1])
                table[row_index][col_index] = grid[row_index][col_index] + min_prev
        return table[-1][-1]

    def test_minPathSum(self):
        grid = [
            [1, 2, 0],
            [2, 1, 0],
            [2, 0, 1]
        ]
        self.assertEqual(self.minPathSum(grid), 4)

    def uniquePathsWithObstacles(self, obstacleGrid):
        row_num = len(obstacleGrid)
        col_num = len(obstacleGrid[0])

        table = []
        for row in range(row_num):
            table.append([0] * (col_num))

        for i in xrange(row_num):
            for j in xrange(col_num):
                if not i:
                    if obstacleGrid[i][j]:
                        break
                    table[i][j] = 1
                    continue
                if not j:
                    if not obstacleGrid[i][j] and table[i-1][j]:
                        table[i][j] = 1
                    continue

                if obstacleGrid[i][j]:
                    continue

                table[i][j] = table[i-1][j] + table[i][j-1]

        return table[-1][-1]

    def test_uniquePathsWithObstacles(self):
        grid = [
            [0,0,1],
            [0,0,0],
            [1,0,0]
        ]
        self.assertEqual(self.uniquePathsWithObstacles(grid), 4)
        grid = [
            [1],
            [0]
        ]
        self.assertEqual(self.uniquePathsWithObstacles(grid), 0)
        grid = [
                [0,1,0,0,0],
                [1,0,0,0,0],
                [0,0,0,0,0],
                [0,0,0,0,0]
        ]
        self.assertEqual(self.uniquePathsWithObstacles(grid), 0)

    def isSymmetric(self, root):

        if not root:
            return True

        def helper(left, right):
            if not left and not right:
                return True
            if not (left and right):
                return False
            if left.val != right.val:
                return False
            return helper(left.left, right.right) and helper(left.right, right.left)

        return helper(root.left, root.right)

    def test_isSymmetric(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(4)
        root.right.left = TreeNode(4)
        root.right.right = TreeNode(3)

        self.assertEqual(self.isSymmetric(root), True)

    def minDepth(self, root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        if not root.left:
            return self.minDepth(root.right) + 1
        if not root.right:
            return self.minDepth(root.left) + 1

        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

    def test_minDepth(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        root.left.left = TreeNode(3)
        root.right.right = TreeNode(3)
        self.assertEqual(self.minDepth(root), 3)

        root = TreeNode(1)
        self.assertEqual(self.minDepth(root), 1)

        root = TreeNode(1)
        root.left = TreeNode(2)
        self.assertEqual(self.minDepth(root), 2)

        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        self.assertEqual(self.minDepth(root), 2)

    def isInterleave(self, s1, s2, s3):
        len_s1 = len(s1)
        len_s2 = len(s2)
        len_s3 = len(s3)

        if len_s1 + len_s2 != len_s3:
            return False

        match = []
        for i in range(len_s1+1):
            match.append([False] * (len_s2+1))

        for i in range(len_s1+1):
            for j in range(len_s2+1):
                if not i and not j:
                    match[i][j] = True
                elif i > 0 and match[i-1][j] and s3[i+j-1] == s1[i-1]:
                    match[i][j] = True
                elif j > 0 and match[i][j-1] and s3[i+j-1] == s2[j-1]:
                    match[i][j] = True
                else:
                    match[i][j] = False

        return match[-1][-1]

    def test_isInterleave(self):
        s1 = 'aabcc'
        s2 = 'dbbca'
        self.assertTrue(self.isInterleave(s1,s2,'aadbbcbcac'))
        self.assertFalse(self.isInterleave(s1,s2,'aadbbbaccc'))


if __name__ == "__main__":
    unittest.main()
