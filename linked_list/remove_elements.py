# -*- coding: utf-8 -*-


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return

        _head = ListNode(-1)
        _head.next = head

        ptr_pre = _head
        ptr = head

        while ptr:
            if ptr.val != val:
                ptr_pre = ptr_pre.next
            else:
                ptr_pre.next = ptr.next
            ptr = ptr.next
        return _head.next
