#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

__author__ = 'lycheng'
__email__ = "lycheng997@gmail.com"

from public import ListNode, list_to_linked, linked_to_list

import unittest

class Solution(unittest.TestCase):

    def search(self, A, target):
        l, r = 0, len(A) - 1
        while l <= r:
            mid = (l + r) / 2
            if target == A[mid]:
                return True
            if A[mid] > A[l]:
                if A[l] <= target and target < A[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            elif A[mid] < A[l]:
                if A[mid] > target or target >= A[l]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                l += 1

        return False

    def test_search(self):
        src = [5, 1, 3]
        self.assertEqual(self.search(src, 3), True)

    def insertionSortList(self, head):
        if not head or not head.next:
            return head
        pre_head = ListNode(-99999999999)
        pre_head.next = head

        it = head

        while it.next:
            if it.next.val < it.val:
                pre = pre_head
                while pre.next.val < it.next.val:
                    pre = pre.next
                tmp = it.next
                it.next = tmp.next
                tmp.next = pre.next
                pre.next = tmp

            else:
                it = it.next

        return pre_head.next

    def test_insertionSortList(self):
        li = [5, 4, 3, 2, 1]
        rv = self.insertionSortList(list_to_linked(li))

        self.assertEqual(linked_to_list(rv), [1, 2, 3, 4, 5])

if __name__ == "__main__":
    unittest.main()
