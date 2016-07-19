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
