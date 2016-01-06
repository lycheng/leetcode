# -*- coding: utf-8 -*-

import unittest

from array_function import contains_duplicate


class TestArray(unittest.TestCase):

    def test_containsDuplicate(self):
        '''
        '''
        so = contains_duplicate.Solution()

        a = None
        self.assertFalse(so.containsDuplicate(a))

        a = [1, 2, 3, 4]
        self.assertFalse(so.containsDuplicate(a))

        a = [1, 2, 3, 4, 1, 1]
        self.assertTrue(so.containsDuplicate(a))

    def test_containsDuplicate_ii(self):
        '''
        '''
        so = contains_duplicate.Solution()

        a = None
        self.assertFalse(so.containsDuplicate_ii(a, 1))

        a = [1, 2, 3, 4]
        self.assertFalse(so.containsDuplicate_ii(a, 1))

        a = [1, 2, 3, 4, 1, 1]
        self.assertTrue(so.containsDuplicate_ii(a, 1))

        a = [1, 2, 3, 4, 1]
        self.assertFalse(so.containsDuplicate_ii(a, 2))
        self.assertTrue(so.containsDuplicate_ii(a, 4))
