#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

__author__ = 'lycheng'
__email__ = "lycheng997@gmail.com"


from public import ListNode

import unittest

class Solution(unittest.TestCase):

    def getIntersectionNode(self, headA, headB):
        ''' https://oj.leetcode.com/problems/intersection-of-two-linked-lists/
        '''

        def get_len_and_tail(head):
            ret = 0
            node = head
            while node:
                ret += 1
                if not node.next:
                    return ret, node
                node = node.next
        if not headA or not headB:
            return None

        len_a, tail_a = get_len_and_tail(headA)
        len_b, tail_b = get_len_and_tail(headB)
        if tail_a != tail_b:
            return None

        a = headA
        b = headB
        if len_a > len_b:
            diff = len_a - len_b
            while diff:
                a = a.next
                diff -= 1
        else:
            diff = len_b - len_a
            while diff:
                b = b.next
                diff -= 1

        for _i in range(min(len_a, len_b)):
            if a == b:
                return a
            a = a.next
            b = b.next

    def test_getIntersectionNode(self):
        c1 = ListNode(0)
        a1 = ListNode(1)
        a1.next = ListNode(2)
        a1.next.next = c1
        b1 = ListNode(1)
        b1.next = ListNode(2)
        b1.next.next = ListNode(3)
        b1.next.next.next = c1
        c1.next = ListNode(-1)
        c1.next.next = ListNode(-2)

        self.assertEqual(0, self.getIntersectionNode(a1, b1).val)









if __name__ == "__main__":
    unittest.main()
