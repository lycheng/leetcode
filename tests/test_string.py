# -*- coding: utf-8 -*-

import unittest


class TestString(unittest.TestCase):

    def test_isSameTree(self):
        ''' test isSameTree
        '''
        from string_func.reverse_words import Solution
        src = "the sky is blue"
        dst = "blue is sky the"

        s = Solution()
        self.assertEqual(dst, s.reverseWords(src))
