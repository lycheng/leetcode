#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

__author__ = 'lycheng'
__email__ = "lycheng997@gmail.com"

# from public import TreeNode

import unittest

class Solution(unittest.TestCase):
    def numDecodings(self, s):
        if not s or s[0] == "0":
            return 0
        len_s = len(s)
        dp = [1, 1]
        for i in range(2, len_s+1):
            if 10 <= int(s[i-2:i]) <= 26 and int(s[i-1]) > 0:
                dp.append(dp[-2] + dp[-1])
            elif 10 <= int(s[i-2:i]) <= 26:
                dp.append(dp[-2])
            elif '1' <= s[i-1] <= '9':
                dp.append(dp[-1])
            else:
                return 0

        return dp[-1]

    def test_numDecodings(self):
        self.assertEqual(3, self.numDecodings("123"))
        self.assertEqual(2, self.numDecodings("12"))
        self.assertEqual(1, self.numDecodings("01"))


if __name__ == "__main__":
    unittest.main()
