# -*- coding: utf-8 -*-

import unittest

from game import nim_game


class TestDesign(unittest.TestCase):

    def test_nim_game(self):
        so = nim_game.Solution()
        self.assertFalse(so.canWinNim(4))
        self.assertTrue(so.canWinNim(5))
