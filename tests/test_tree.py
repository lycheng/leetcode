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

    def test_treeTraversal(self):
        ''' test inorderTraversal
        '''
        from tree.binary_tree_traversal import Solution
        so = Solution()

        p = TreeNode(1)
        p.left = TreeNode(2)
        p.right = TreeNode(3)

        self.assertEqual(so.inorderTraversal(p), [2, 1, 3])
        self.assertEqual(so.preorderTraversal(p), [1, 2, 3])
        self.assertEqual(so.postorderTraversal(p), [2, 3, 1])

    def test_binaryTreePaths(self):
        ''' test binaryTreePaths
        '''
        from tree.binary_tree_paths import Solution

        so = Solution()
        root = TreeNode(1)
        paths = so.binaryTreePaths(root)
        self.assertEqual(1, len(paths))
        self.assertTrue('1', paths)

        root.left = TreeNode(2)
        root.right = TreeNode(3)

        paths = so.binaryTreePaths(root)

        self.assertEqual(2, len(paths))
        self.assertTrue('1->2', paths)
        self.assertTrue('1->3', paths)

        paths = so.binaryTreePaths(None)
        self.assertEqual(0, len(paths))

    def test_lowestCommonAncestor(self):

        from tree.lowest_common_ancestor import Solution
        so = Solution()
        node6 = TreeNode(6)
        node2 = TreeNode(2)
        node8 = TreeNode(8)
        node0 = TreeNode(0)
        node4 = TreeNode(4)
        node3 = TreeNode(3)
        node5 = TreeNode(5)
        node8 = TreeNode(8)
        node7 = TreeNode(7)
        node9 = TreeNode(9)

        node6.left = node2
        node6.right = node8
        node6.left.left = node0
        node6.left.right = node4
        node6.left.right.left = node3
        node6.left.right.right = node5
        node6.right.left = node7
        node6.right.right = node9

        self.assertEqual(so.lowestCommonAncestor(node6, node8, node2), node6)
        self.assertEqual(so.lowestCommonAncestor(node6, node4, node2), node2)
