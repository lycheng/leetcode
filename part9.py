#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

__author__ = 'lycheng'
__email__ = "lycheng997@gmail.com"

import unittest

class Solution(unittest.TestCase):

    def search(self, A, target):
        l, r = 0, len(A) - 1
        while l <= r:
            mid = (l + r) / 2
            if target == A[mid]:
                return True
            if A[mid] > A[l]:
                if A[l] <= target and target < A[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            elif A[mid] < A[l]:
                if A[mid] > target or target >= A[l]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                l += 1

        return False

    def test_search(self):
        src = [5, 1, 3]
        self.assertEqual(self.search(src, 3), True)

if __name__ == "__main__":
    unittest.main()
