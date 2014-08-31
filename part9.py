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

    def grayCode(self, n):
        if not n:
            return [0]
        rv = []
        limit = 1 << n
        for i in xrange(limit):
            rv.append(i ^ (i >> 1))

        return rv

    def test_grayCode(self):
        rv = sorted(self.grayCode(0))
        self.assertEqual([0], rv)

        rv = sorted(self.grayCode(1))
        self.assertEqual([0, 1], rv)


        rv = sorted(self.grayCode(2))
        self.assertEqual([0, 1, 2, 3], rv)

        rv = sorted(self.grayCode(3))
        self.assertEqual(sorted([0,1,3,2,6,7,5,4]), rv)

    def singleNumber(self, A):
        num_len = 32
        bits = [0 for i in range(num_len)]
        for x in xrange(num_len):
            count = 0
            for num in A:
                count += ((num >> x) & 1)
            bits[num_len - 1 - x] = count % 3

        neg = False
        if bits[0]:
            neg = True

        if neg:
            bits = "".join([str(1 - bit) for bit in bits])
            result = -(int(bits, 2) + 1)
        else:
            bits = "".join([str(bit) for bit in bits])
            result = int(bits, 2)

        return result

    def test_singleNumber(self):
        src = [1, 1, 1, 2, 2, 2, 3]
        self.assertEqual(3, self.singleNumber(src))

        src = [-2,-2,1,1,-3,1,-3,-3,-4,-2]
        self.assertEqual(-4, self.singleNumber(src))

    def maxArea(self, height):
        beg = 0
        end = len(height) - 1
        result = min(height[beg], height[end]) * (end - beg)

        while beg < end:
            cur = min(height[beg], height[end]) * (end - beg)
            if cur > result:
                result = cur

            if height[beg] < height[end]:
                beg += 1
            else:
                end -= 1

        return result

    def test_maxArea(self):
        h = [1, 2]
        self.assertEqual(1, self.maxArea(h))

        h = [1, 2, 3, 4, 5, 6, 7, 8]
        self.assertEqual(16, self.maxArea(h))



if __name__ == "__main__":
    unittest.main()
