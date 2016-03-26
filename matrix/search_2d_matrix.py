# -*- coding: utf-8 -*-

'''

https://leetcode.com/problems/search-a-2d-matrix/
https://leetcode.com/problems/search-a-2d-matrix-ii/
'''


class Solution(object):

    def searchMatrix_i(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False

        for row in matrix:
            if target < row[0]:
                return False
            if target > row[-1]:
                continue
            if target in row:
                return True

        return False

    def searchMatrix_ii(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False

        len_matrix = len(matrix)
        ridx = 0

        while ridx < len_matrix:
            row = matrix[ridx]
            if target < row[0]:
                return False
            if target > row[-1]:
                ridx += 1
                continue

            j = 0
            for cidx, val in enumerate(row):
                if val == target:
                    return True

                if val < target:
                    j = cidx
                    continue
                break

            for i in range(ridx, len(matrix)):
                if matrix[i][j] < target:
                    continue
                if matrix[i][j] == target:
                    return True
                break
            ridx += 1

        return False

    def searchMatrix_ii_submisson2(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False

        len_matrix = len(matrix)
        ridx = 0
        cidx = len(matrix[0]) - 1

        while ridx < len_matrix and cidx >= 0:
            val = matrix[ridx][cidx]
            if val == target:
                return True

            if val > target:
                cidx -= 1

            if val < target:
                ridx += 1

        return False
