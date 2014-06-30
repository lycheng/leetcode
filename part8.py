#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

__author__ = 'lycheng'
__email__ = "lycheng997@gmail.com"

from public import linked_to_list, list_to_linked, ListNode, TreeNode

import unittest

class Solution(unittest.TestCase):

    def rotate(self, matrix):

        n = len(matrix)

        for i in range(n):
            for j in range(n):
                if i + j >= n -1:
                    continue
                matrix[i][j], matrix[n-1-j][n-1-i] = \
                        matrix[n-1-j][n-1-i], matrix[i][j]

        for i in range(n/2):
            matrix[i], matrix[n-1-i] = matrix[n-1-i], matrix[i]

        return matrix


    def test_rotate(self):
        matrix = [
            [1, 2],
            [3, 4]
        ]
        self.assertEqual(self.rotate(matrix), [[3, 1], [4, 2]])

        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]
        self.assertEqual(self.rotate(matrix), [[7, 4, 1], [8, 5, 2],[9, 6, 3]])

    def deleteDuplicates(self, head):
        if not head:
            return head

        new_head = ListNode(-1)
        new_head.next = head

        pre = new_head
        now = head

        while now and now.next:
            if now.next.val == now.val:
                while now.next and now.val == now.next.val:
                    now = now.next
                pre.next = now.next
            else:
                pre = now
            now = now.next

        return new_head.next

    def test_deleteDuplicates(self):
        src = [1, 1, 2, 3]
        root = list_to_linked(src)
        head = self.deleteDuplicates(root)
        self.assertEqual(linked_to_list(head), [2, 3])

    def isValidBST(self, root):
        def helper(root, min_val, max_val):
            if not root:
                return True

            if root.val >= max_val or root.val <= min_val:
                return False

            return helper(root.left, min_val, root.val) and helper(root.right, root.val, max_val)


        if not root:
            return True

        min_val = -999999999999
        max_val = -min_val

        return helper(root, min_val, max_val)

    def test_isValidBST(self):

        root = TreeNode(8)
        root.left = TreeNode(3)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(6)
        root.left.right.left = TreeNode(4)
        root.left.right.right = TreeNode(7)
        root.right = TreeNode(10)
        root.right.right = TreeNode(14)
        root.right.right.left = TreeNode(13)

        self.assertTrue(self.isValidBST(root))


if __name__ == "__main__":
    unittest.main()
