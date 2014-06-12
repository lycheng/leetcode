#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

__author__ = 'lycheng'
__email__ = "lycheng997@gmail.com"

from public import TreeNode

class Solution(object):

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

        print self.pathSum(root, 22)

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

                # for row in table:
                    # print row
                # print "--"
        return table[-1][-1]

    def test_minPathSum(self):
        grid = [
            [1, 2, 0],
            [2, 1, 0],
            [2, 0, 1]
        ]
        print self.minPathSum(grid)

    def uniquePathsWithObstacles(self, obstacleGrid):
        row_num = len(obstacleGrid)
        col_num = len(obstacleGrid[0])

        table = []
        for row in range(row_num):
            table.append([0] * (col_num))

        for i in xrange(row_num):
            for j in xrange(col_num):

                # for row in table:
                    # print row
                # print "--"

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
        print self.uniquePathsWithObstacles(grid)
        grid = [
            [1],
            [0]
        ]
        print self.uniquePathsWithObstacles(grid)
        grid = [
                [0,1,0,0,0],
                [1,0,0,0,0],
                [0,0,0,0,0],
                [0,0,0,0,0]
        ]
        print self.uniquePathsWithObstacles(grid)


if __name__ == "__main__":
    so = Solution()
    # so.test_pathSum()
    # print so.removeDuplicates([1, 1, 2, 2, 3])
    # so.test_minPathSum()
    so.test_uniquePathsWithObstacles()
