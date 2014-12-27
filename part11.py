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

    def majorityElement(self, num):
        count_map = {}
        majority = None
        majority_times = 0

        for n in num:
            if n not in count_map:
                count_map[n] = 0
            count_map[n] += 1

            if count_map[n] > majority_times:
                majority_times = count_map[n]
                majority = n

        return majority

    def test_majorityElement(self):
        num = [1, 2, 3, 4, 1, 1, 1]
        self.assertEqual(self.majorityElement(num), 1)

    def convertToTitle(self, num):
        ascii_table = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        result = []
        while num:
            r = num % 26
            num /= 26
            result.append(ascii_table[r-1])
            if not r:
                num -= 1
        return "".join(result[::-1])


    def test_convertToTitle(self):
        self.assertEqual(self.convertToTitle(26), 'Z')
        self.assertEqual(self.convertToTitle(27), 'AA')

    def compareVersion(self, version1, version2):
        longer = version1.split('.')
        shorter = version2.split('.')
        flag = 1

        if len(longer) < len(shorter):
            longer, shorter = shorter, longer
            flag = -1

        for idx in range(len(longer)):
            longer_item = int(longer[idx])
            if idx >= len(shorter):
                if not longer_item:
                    shorter.append(0)
                    continue
                return flag
            elif longer_item > int(shorter[idx]):
                return flag
            elif longer_item < int(shorter[idx]):
                return -flag

        if len(longer) == len(shorter):
            return 0

    def test_compareVersion(self):
        self.assertEqual(self.compareVersion('2.1', '1.1'), 1)
        self.assertEqual(self.compareVersion('1.1', '1.1'), 0)
        self.assertEqual(self.compareVersion('1.1', '2.1'), -1)
        self.assertEqual(self.compareVersion('1', '1.1'), -1)
        self.assertEqual(self.compareVersion('1.0', '1'), 0)

if __name__ == "__main__":
    unittest.main()
