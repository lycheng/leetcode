# -*- coding: utf-8 -*-

import unittest


class TestBit(unittest.TestCase):

    def test_word_pattern(self):

        from hash_func.word_pattern import Solution

        input_output = [
            ('abba', 'dog cat cat dog', True),
            ('abba', 'dog cat cat fish', False),
            ('aaaa', 'dog cat cat dog', False),
            ('abba', 'dog dog dog dog', False)
        ]

        so = Solution()
        for pattern, s, result in input_output:
            self.assertEqual(so.wordPattern(pattern, s), result)
