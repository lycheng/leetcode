#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

__author__ = 'lycheng'
__email__ = "lycheng997@gmail.com"

from public import linked_to_list, list_to_linked

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


if __name__ == "__main__":
    unittest.main()
