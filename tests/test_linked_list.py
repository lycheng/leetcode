# -*- coding: utf-8 -*-

import unittest

from linked_list import (delete_node, list_cycle, remove_elements,
                         reverse_list)
from public import ListNode


class TestLinkedList(unittest.TestCase):

    def test_delete_node(self):
        so = delete_node.Solution()

        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        so.deleteNode(head.next)

        self.assertEqual(head.next.val, 3)

    def test_has_cycle(self):
        so = list_cycle.Solution()
        self.assertFalse(so.hasCycle(None))

        head = ListNode(1)
        self.assertFalse(so.hasCycle(head))

        head.next = head
        self.assertTrue(so.hasCycle(head))

        head.next = ListNode(2)
        head.next.next = ListNode(3)
        self.assertFalse(so.hasCycle(head))

        head.next.next.next = head
        self.assertTrue(so.hasCycle(head))

    def test_detect_cycle(self):
        so = list_cycle.Solution()

        head = ListNode(1)
        self.assertFalse(so.detectCycle(head))
        self.assertFalse(so.detectCycle(None))

        head.next = ListNode(2)
        self.assertFalse(so.detectCycle(head))

        cross = ListNode(3)
        head.next.next = cross
        head.next.next.next = ListNode(4)
        head.next.next.next.next = ListNode(5)
        head.next.next.next.next.next = cross

        self.assertEqual(so.detectCycle(head), cross)

    def test_remove_elements(self):
        so = remove_elements.Solution()
        self.assertFalse(so.removeElements(None, 0))

        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(2)
        head.next.next.next = ListNode(3)
        head.next.next.next.next = ListNode(4)

        head = so.removeElements(head, 1)
        self.assertEqual(head.val, 2)

        head = so.removeElements(head, 2)
        self.assertEqual(head.val, 3)

        head = so.removeElements(head, 4)

        self.assertFalse(head.next)

    def test_reverse_linked_list(self):
        so = reverse_list.Solution()
        self.assertFalse(so.reverseList_iteratively(None))

        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        self.assertEqual(so.reverseList_iteratively(head).val, 3)

        self.assertFalse(so.reverseList_recursively(None))
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        self.assertEqual(so.reverseList_recursively(head).val, 3)
