# -*- coding: utf-8 -*-

import unittest

from others import count_primes


class TestDesign(unittest.TestCase):

    def test_nim_game(self):
        so = count_primes.Solution()

        self.assertEqual(so.countPrimes(2), 0)
        self.assertEqual(so.countPrimes(3), 1)
        self.assertEqual(so.countPrimes(4), 2)
        self.assertEqual(so.countPrimes(5), 2)
        self.assertEqual(so.countPrimes(10), 4)
