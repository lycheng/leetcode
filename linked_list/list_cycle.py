# -*- coding: utf-8 -*-

__author__ = 'lycheng'
__email__ = "lycheng997@gmail.com"


class Solution(object):

    def hasCycle(self, head):
        """ https://leetcode.com/problems/linked-list-cycle/

        :type head: ListNode
        :rtype: bool
        """

        if not head or not head.next:
            return False

        slow_ptr = head
        fast_ptr = head.next.next

        while fast_ptr:
            if slow_ptr == fast_ptr:
                return True
            slow_ptr = slow_ptr.next
            if not fast_ptr.next or not fast_ptr.next.next:
                break

            fast_ptr = fast_ptr.next.next
        return False

    def detectCycle(self, head):
        """ https://leetcode.com/problems/linked-list-cycle-ii/
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return None

        fast = head
        slow = head
        while fast and slow:
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
            if fast == slow:
                break

        if not fast:
            return None

        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return fast
