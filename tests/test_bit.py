# -*- coding: utf-8 -*-

import unittest


class TestBit(unittest.TestCase):

    def test_number_of_1_bits(self):

        from bit.number_of_1_bits import Solution

        input_output = [
            (1, 1),
            (2, 1),
            (3, 2),
            (4, 1)
        ]

        so = Solution()
        for i, o in input_output:
            self.assertEqual(so.hammingWeight(i), o)
