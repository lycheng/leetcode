#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

__author__ = 'lycheng'
__email__ = "lycheng997@gmail.com"

from public import linked_to_list, list_to_linked
from public import TreeNode

import unittest

class Solution(unittest.TestCase):
    def numDecodings(self, s):
        if not s or s[0] == "0":
            return 0
        len_s = len(s)
        dp = [1, 1]
        for i in range(2, len_s+1):
            if 10 <= int(s[i-2:i]) <= 26 and int(s[i-1]) > 0:
                dp.append(dp[-2] + dp[-1])
            elif 10 <= int(s[i-2:i]) <= 26:
                dp.append(dp[-2])
            elif '1' <= s[i-1] <= '9':
                dp.append(dp[-1])
            else:
                return 0

        return dp[-1]

    def test_numDecodings(self):
        self.assertEqual(3, self.numDecodings("123"))
        self.assertEqual(2, self.numDecodings("12"))

    def removeNthFromEnd(self, head, n):
        ahead = head
        behind = head

        steps = 0  # handle head node
        for i in range(n+1):
            if ahead:
                ahead = ahead.next
                steps += 1

        while ahead:
            ahead = ahead.next
            behind = behind.next

        if steps == n: # handle head node:
            head = head.next
        else:
            need_to_remove_node = behind.next
            behind.next = need_to_remove_node.next
            need_to_remove_node.next = None

        return head

    def test_removeNthFromEnd(self):
        src = [1, 2, 3, 4, 5]
        head = list_to_linked(src)
        rv = self.removeNthFromEnd(head, 2)
        self.assertEqual(linked_to_list(rv), [1, 2, 3, 5])

        src = [1]
        head = list_to_linked(src)
        rv = self.removeNthFromEnd(head, 1)
        self.assertEqual(linked_to_list(rv), [])

    def removeDuplicates(self, A):
        length = len(A)
        if length <= 2:
            return length

        index = 1
        for behind in range(2, length):
            if A[behind] == A[index] and A[behind] == A[index-1]:
                continue
            index += 1
            A[index] = A[behind]
        return index + 1

    def test_removeDuplicates(self):
        self.assertEqual(self.removeDuplicates([1, 2, 3]), 3)
        self.assertEqual(self.removeDuplicates([1, 1, 3]), 3)
        self.assertEqual(self.removeDuplicates([1, 1, 3, 4]), 4)
        self.assertEqual(self.removeDuplicates([1, 1, 1, 4]), 3)
        self.assertEqual(self.removeDuplicates([1,1,1,2,2,3]), 5)

    def levelOrder(self, root):
        rv = []
        if not root:
            return rv
        rv.append([root.val])
        cur_level = [root]
        next_level = []
        while cur_level:
            node = cur_level.pop(0)
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)

            if not cur_level:
                if not next_level:
                    break
                rv.append([n.val for n in next_level])
                cur_level = next_level
                next_level = []

        return rv

    def test_levelOrder(self):
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)

        rv = self.levelOrder(root)
        self.assertEqual(rv, [[3],[9,20],[15,7]])

    def addBinary(self, a, b):

        if len(a) < len(b):
            a, b = b, a

        diff_len = len(a) - len(b)
        if diff_len:
            b = ('0' * diff_len) + b

        carry = 0
        result = []
        for i in range(len(a) - 1, -1, -1):
            r = int(a[i]) + int(b[i]) + carry
            if r > 1:
                result.append(str(r % 2))
                carry = 1
            else:
                result.append(str(r))
                carry = 0
        if carry:
            result.append('1')

        return ''.join(result[::-1])


    def test_addBinary(self):
        r = self.addBinary('11', '110')
        self.assertEqual(r, '1001')

        r = self.addBinary('1', '1')
        self.assertEqual(r, '10')

        r = self.addBinary('11', '1')
        self.assertEqual(r, '100')

        r = self.addBinary('1111', '1111')
        self.assertEqual(r, '11110')

if __name__ == "__main__":
    unittest.main()
