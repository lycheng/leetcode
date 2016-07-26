# -*- coding: utf-8 -*-


class NumMatrix(object):
    ''' https://leetcode.com/problems/range-sum-query-2d-immutable/
    '''

    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        self.matrix_sum = []
        if not matrix:
            return

        width = len(matrix[0])
        height = len(matrix)
        self.matrix_sum = [[0 for x in range(width+1)]
                           for y in range(height+1)]

        for i in range(1, height+1):
            for j in range(1, width+1):
                self.matrix_sum[i][j] += self.matrix_sum[i-1][j] + \
                    self.matrix_sum[i][j-1] - self.matrix_sum[i-1][j-1] + \
                    matrix[i-1][j-1]

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if not self.matrix_sum:
            return 0
        return self.matrix_sum[row2+1][col2+1] - \
            self.matrix_sum[row1][col2+1] - \
            self.matrix_sum[row2+1][col1] + \
            self.matrix_sum[row1][col1]
