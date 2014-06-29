#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

__author__ = 'lycheng'
__email__ = "lycheng997@gmail.com"

import unittest

class Solution(unittest.TestCase):

    def rotate(self, matrix):

        n = len(matrix)

        for i in range(n):
            for j in range(n):
                if i + j >= n -1:
                    continue
                matrix[i][j], matrix[n-1-j][n-1-i] = \
                        matrix[n-1-j][n-1-i], matrix[i][j]

        for i in range(n/2):
            matrix[i], matrix[n-1-i] = matrix[n-1-i], matrix[i]

        return matrix


    def test_rotate(self):
        matrix = [
            [1, 2],
            [3, 4]
        ]
        self.assertEqual(self.rotate(matrix), [[3, 1], [4, 2]])

        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]
        self.assertEqual(self.rotate(matrix), [[7, 4, 1], [8, 5, 2],[9, 6, 3]])


if __name__ == "__main__":
    unittest.main()
