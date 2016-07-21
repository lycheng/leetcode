# -*- coding: utf-8 -*-

import unittest


class TestDesign(unittest.TestCase):

    def test_nim_game(self):
        from game import nim_game
        so = nim_game.Solution()
        self.assertFalse(so.canWinNim(4))
        self.assertTrue(so.canWinNim(5))

    def test_guess_number(self):
        from game import guess_number

        so = guess_number.Solution()

        guess_number.TARGET = 6
        self.assertTrue(so.guessNumber(10), 6)

    def test_bulls_and_cows(self):

        from game import bulls_and_cows

        so = bulls_and_cows.Solution()
        resources = [
            ("1807", "7810", "1A3B"),
            #  ("1123", "0111", "1A1B"),
            #  ("1122", "1222", "3A0B")
        ]

        for secret, guess, result in resources:
            self.assertEqual(so.getHint(secret, guess), result)
