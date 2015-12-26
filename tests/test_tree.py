# -*- coding: utf-8 -*-

import unittest

from public import TreeNode


class TestTree(unittest.TestCase):

    def test_isSameTree(self):
        ''' test isSameTree
        '''
        from tree.same_tree import Solution
        o = Solution()
        p = None
        q = None
        self.assertTrue(o.isSameTree(p, q))

        p = TreeNode(1)
        p.left = TreeNode(2)
        self.assertFalse(o.isSameTree(p, q))

        q = TreeNode(1)
        q.left = TreeNode(2)
        self.assertTrue(o.isSameTree(p, q))

        q.left = TreeNode(3)
        self.assertFalse(o.isSameTree(p, q))

    def test_invertTree(self):
        ''' test invertTree
        '''
        from tree.invert_binary_tree import Solution
        o = Solution()

        p = TreeNode(1)
        p.left = TreeNode(2)
        p.right = TreeNode(3)

        ret = o.invertTree(p)
        self.assertEqual(ret.left.val, 3)

    def test_maxDepth(self):
        ''' test invertTree
        '''
        from tree.maximum_depth_of_binary_tree import Solution
        o = Solution()

        p = TreeNode(1)
        p.left = TreeNode(2)
        p.right = TreeNode(3)

        self.assertEqual(o.maxDepth(p), 2)
