#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

__author__ = 'lycheng'
__email__ = "lycheng997@gmail.com"

from public import ListNode, list_to_linked, linked_to_list

import unittest
import time

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

    def divide(self, dividend, divisor):

        if not dividend:
            return 0
        sign = 1 if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0) else -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        k = 0
        tmp = divisor
        while dividend > tmp:
            tmp <<= 1
            k += 1

        if tmp == dividend:
            return (1 << k) * sign

        k -= 1
        tmp >>= 1
        rv = 0
        while dividend >= divisor:
            if dividend >= tmp:
                rv += 1 << k
                dividend -= tmp
            tmp >>= 1
            k -= 1

        return rv * sign

    def test_divide(self):
        self.assertEqual(2, self.divide(4, 2))
        self.assertEqual(7, self.divide(14, 2))
        self.assertEqual(7, self.divide(15, 2))
        self.assertEqual(-1, self.divide(-1, 1))
        self.assertEqual(0, self.divide(1, 2))
        self.assertEqual(2147483647, self.divide(2147483647, 1))
        self.assertEqual(715827882, self.divide(2147483647, 3))
        self.assertEqual(6, self.divide(19, 3))

    def setZeroes(self, matrix):

        clear_first_row = 0 in matrix[0]
        clear_first_column = 0 in [row[0] for row in matrix]

        for r_idx, _v in enumerate(matrix):
            for c_idx, _v in enumerate(matrix[r_idx]):
                if matrix[r_idx][c_idx]:
                    continue
                matrix[r_idx][0] = 0
                matrix[0][c_idx] = 0


        for idx, val in enumerate(matrix[0]):
            if val or not idx:
                continue
            for j in range(len(matrix)):
                matrix[j][idx] = 0

        for idx, val in enumerate([row[0] for row in matrix]):
            if val or not idx:
                continue
            for j in range(len(matrix[0])):
                matrix[idx][j] = 0

        if clear_first_row:
            for idx, val in enumerate(matrix[0]):
                matrix[0][idx] = 0
        if clear_first_column:
            for idx, val in enumerate([row[0] for row in matrix]):
                matrix[idx][0] = 0
        return matrix

    def test_setZeroes(self):
        matrix = [[0]]
        self.assertEqual([[0]], self.setZeroes(matrix))

        matrix = [
            [0, 1, 2],
            [1, 0, 2],
            [3, 1, 2],
        ]
        result = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 2],
        ]
        self.assertEqual(result, self.setZeroes(matrix))

        matrix = [
            [1, 1, 2],
            [1, 0, 2],
            [3, 1, 2],
        ]
        result = [
            [1, 0, 2],
            [0, 0, 0],
            [3, 0, 2],
        ]
        self.assertEqual(result, self.setZeroes(matrix))

    def longestPalindrome(self, s):
        # len_s = len(s)
        # if len_s <= 1:
            # return s
        # m = [[False] * len_s for i in s]
        # max_len = 0
        # beg = 0
        # end = 1
        # for j in range(1, len_s):
            # for i in range(j):
                # m[i][j] = (s[i] == s[j]) and (j - i < 2 or m[i+1][j-1])
                # if m[i][j] and j - i + 1 > max_len:
                    # beg = i
                    # end = j
                    # max_len = j - i + 1
                # # use for j - i == 2
                # m[j][j] = True

        # return s[beg:end+1]
        # the code above time Exceeded
        def get_longest_palindrome(self, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1: r]

        rv = ''
        for i in range(len(s)):
            s1 = get_longest_palindrome(s, i, i)
            if len(s1) > len(rv):
                rv = s1
            s2 = get_longest_palindrome(s, i, i + 1)
            if len(s2) > len(rv):
                rv = s2

        return rv

    def test_longestPalindrome(self):
        s = '123321'
        self.assertEqual(s, self.longestPalindrome(s))
        s = '12321'
        self.assertEqual(s, self.longestPalindrome(s))
        s = 'aaaabaaa'
        self.assertEqual('aaabaaa', self.longestPalindrome(s))
        s = 'abb'
        self.assertEqual('bb', self.longestPalindrome(s))


        b = time.time()
        s = 'a' * 1000
        self.longestPalindrome(s)
        print time.time() - b


if __name__ == "__main__":
    unittest.main()
