# -*- coding: utf-8 -*-

import unittest

from others import (count_primes, add_digits, move_zeroes, valid_anagram)


class TestDesign(unittest.TestCase):

    def test_nim_game(self):
        so = count_primes.Solution()

        self.assertEqual(so.countPrimes(2), 0)
        self.assertEqual(so.countPrimes(3), 1)
        self.assertEqual(so.countPrimes(4), 2)
        self.assertEqual(so.countPrimes(5), 2)
        self.assertEqual(so.countPrimes(10), 4)

    def test_add_digits(self):
        so = add_digits.Solution()

        self.assertEqual(so.addDigits(38), 2)
        self.assertEqual(so.addDigits(9), 9)
        self.assertEqual(so.addDigits(0), 0)

    def test_move_zeroes(self):
        so = move_zeroes.Solution()

        src = [0, 1, 0, 3, 12]
        dst = [1, 3, 12, 0, 0]
        so.moveZeroes(src)
        self.assertEqual(src, dst)

        src = [1, 0]
        dst = [1, 0]
        so.moveZeroes(src)
        self.assertEqual(src, dst)

        src = [1]
        dst = [1]
        so.moveZeroes(src)
        self.assertEqual(src, dst)

        src = []
        dst = []
        so.moveZeroes(src)
        self.assertEqual(src, dst)

    def test_valid_anagram(self):
        so = valid_anagram.Solution()

        self.assertTrue(so.isAnagram('anagram', 'nagaram'))
        self.assertFalse(so.isAnagram('rat', 'car'))

        self.assertFalse(so.isAnagram('a', 'ab'))
