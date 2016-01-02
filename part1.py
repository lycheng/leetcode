#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

__author__ = 'lycheng'
__email__ = "lycheng997@gmail.com"


class Solution(object):
    def reverseWords(self, s):
        ''' reverseWords
        @param s, a string
        @return a string
        '''
        s = ' '.join(s.split())  # 分割出一个个单词出来
        words = s.split(' ')
        words = [word[::-1] for word in words]
        return " ".join(words)[::-1]

    def singleNumber(self, li):
        ''' return the single num in array
        @param A, a list of integer
        @return an integer
        '''
        rv = reduce(lambda x, y: x ^ y, li)
        return rv

    def reverse(self, x):
        ''' reverse number
        '''

        if x < 0:
            m = -1
        else:
            m = 1
        x = str(x * m)[::-1]
        return m * int(x)

    def searchInsert(self, A, target):
        if target in A:
            return A.index(target)

        while target > A[0]:
            target = target - 1
            if target in A:
                return A.index(target) + 1

        return 0

    def deleteDuplicates(self, head):

        if not head:
            return head

        beg = head
        while head:
            while head.next and head.next.val == head.val:
                head.next = head.next.next
            head = head.next

        return beg

    def climbStairs(self, n):
        if n in [0, 1, 2]:
            return n

        two_step_behind = 1
        one_step_behind = 2
        cur_step = 2
        cur_solution = 0

        while cur_step < n:
            cur_solution = two_step_behind + one_step_behind
            two_step_behind = one_step_behind
            one_step_behind = cur_solution
            cur_step += 1

        return cur_solution

def run():
    o = Solution()
    # print o.reverseWords("    the sky is       blue")
    o.singleNumber([1, 2, 3, 4, 5, 3, 2, 1, 4])


if __name__ == "__main__":
    run()
