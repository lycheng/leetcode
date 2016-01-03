# -*- coding: utf-8 -*-


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def reverseList_iteratively(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return

        _head = ListNode(-1)
        while head:
            _next = head.next
            head.next = _head.next
            _head.next = head
            head = _next

        return _head.next

    def reverseList_recursively(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self._do_reverse_list_recursively(head, None)

    def _do_reverse_list_recursively(self, head, new_head):
        '''
        '''
        if not head:
            return new_head

        _next = head.next
        head.next = new_head
        return self._do_reverse_list_recursively(_next, head)
