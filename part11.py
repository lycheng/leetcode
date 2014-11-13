#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

__author__ = 'lycheng'
__email__ = "lycheng997@gmail.com"

from public import ListNode, TreeNode
from public import list_to_linked, linked_to_list

import unittest

class Solution(unittest.TestCase):

    def sortedListToBST(self, head):
        def get_n_item(head, n):
            i = head
            while n:
                i = i.next
                n -= 1
            return i

        def helper(head, start, end):
            if start > end or not head:
                return None

            mid = (start + end) / 2
            mid_item = get_n_item(head, mid)
            if not mid_item:
                return None
            root = TreeNode(mid_item.val)
            if start != end:
                root.left = helper(head, 0, mid-1)
                root.right = helper(mid_item.next, 0, end-mid-1)
            return root

        if not head:
            return None

        cur = head
        l = 0
        while cur:
            cur = cur.next
            l += 1

        return helper(head, 0, l)

    def test_sortedListToBST(self):
        head = list_to_linked([1, 2, 3])
        root = self.sortedListToBST(head)
        self.assertEqual(2, root.val)
        self.assertEqual(1, root.left.val)
        self.assertEqual(3, root.right.val)

if __name__ == "__main__":
    unittest.main()
