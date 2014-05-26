#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

__author__ = 'lycheng'
__email__ = "lycheng997@gmail.com"

from public import ListNode

class Solution(object):

    def swapPairs(self, head):
        if not head or not head.next:
            return head

        r = head.next
        while head and head.next:
            one_pre = head.next
            two_pre = head.next.next
            one_pre.next = head
            head.next = two_pre
            head = head.next

            if head and head.next:
                one_pre.next.next = head.next

        return r

    def test_swapPairs(self):
        one = ListNode(1)
        two = ListNode(2)
        three = ListNode(3)
        four = ListNode(4)
        one.next = two
        two.next = three
        three.next = four
        r = self.swapPairs(one)

        while r:
            print r.val
            r = r.next

    def connect(self, root):
        if not root or not root.left:
            return root

        l = root.left
        r = root.right
        while l:
            l.next = r
            l = l.right
            r = r.left

        self.connect(root.left)
        self.connect(root.right)

    def permute(self, num):

        length = len(num)
        if length == 0:
            return []
        if length == 1:
            return [num]

        result = []
        for i in range(length):
            for r in self.permute(num[0:i] + num[i+1:]):
                result.append([num[i]] + r)

        return result



    def test_permute(self):

        s = [1, 2, 3, 1]
        print self.permute(s)


if __name__ == "__main__":
    so = Solution()
    so.test_permute()
