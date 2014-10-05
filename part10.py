#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

__author__ = 'lycheng'
__email__ = "lycheng997@gmail.com"

from public import ListNode, TreeNode
from public import list_to_linked, linked_to_list

import unittest

class Solution(unittest.TestCase):

    def zigzagLevelOrder(self, root):
        result = []
        if not root:
            return result

        left_to_right = 0
        result.append([root.val])
        cur_level = [root]
        next_level = []
        while cur_level:
            node = cur_level.pop(0)
            if node.left or node.right:
                next_level.append(node.left)
                next_level.append(node.right)

            if not cur_level:
                if not next_level:
                    break
                cur_level = [n for n in next_level if n]
                if left_to_right:
                    result.append([n.val for n in cur_level])
                else:
                    result.append([n.val for n in reversed(cur_level)])
                left_to_right = left_to_right ^ 1
                next_level = []

        return result

    def test_zigzagLevelOrder(self):
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)

        self.assertEqual([[3], [20, 9], [15, 7]], self.zigzagLevelOrder(root))


if __name__ == "__main__":
    unittest.main()
