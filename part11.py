#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

__author__ = 'lycheng'
__email__ = "lycheng997@gmail.com"

from public import TreeNode
from public import list_to_linked
from public import is_palindrome

import unittest

class Solution(unittest.TestCase):

    def sortedListToBST(self, head):
        def get_n_item(head, n):
            i = head
            while n:
                i = i.next
                n -= 1
            return i

        def helper(head, start, end):
            if start > end or not head:
                return None

            mid = (start + end) / 2
            mid_item = get_n_item(head, mid)
            if not mid_item:
                return None
            root = TreeNode(mid_item.val)
            if start != end:
                root.left = helper(head, 0, mid-1)
                root.right = helper(mid_item.next, 0, end-mid-1)
            return root

        if not head:
            return None

        cur = head
        l = 0
        while cur:
            cur = cur.next
            l += 1

        return helper(head, 0, l)

    def test_sortedListToBST(self):
        head = list_to_linked([1, 2, 3])
        root = self.sortedListToBST(head)
        self.assertEqual(2, root.val)
        self.assertEqual(1, root.left.val)
        self.assertEqual(3, root.right.val)

    def majorityElement(self, num):
        count_map = {}
        majority = None
        majority_times = 0

        for n in num:
            if n not in count_map:
                count_map[n] = 0
            count_map[n] += 1

            if count_map[n] > majority_times:
                majority_times = count_map[n]
                majority = n

        return majority

    def test_majorityElement(self):
        num = [1, 2, 3, 4, 1, 1, 1]
        self.assertEqual(self.majorityElement(num), 1)

    def convertToTitle(self, num):
        '''https://oj.leetcode.com/problems/excel-sheet-column-title/
        '''
        ascii_table = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        result = []
        while num:
            r = num % 26
            num /= 26
            result.append(ascii_table[r-1])
            if not r:
                num -= 1
        return "".join(result[::-1])


    def test_convertToTitle(self):
        self.assertEqual(self.convertToTitle(26), 'Z')
        self.assertEqual(self.convertToTitle(27), 'AA')

    def compareVersion(self, version1, version2):
        longer = version1.split('.')
        shorter = version2.split('.')
        flag = 1

        if len(longer) < len(shorter):
            longer, shorter = shorter, longer
            flag = -1

        for idx in range(len(longer)):
            longer_item = int(longer[idx])
            if idx >= len(shorter):
                if not longer_item:
                    shorter.append(0)
                    continue
                return flag
            elif longer_item > int(shorter[idx]):
                return flag
            elif longer_item < int(shorter[idx]):
                return -flag

        if len(longer) == len(shorter):
            return 0

    def test_compareVersion(self):
        self.assertEqual(self.compareVersion('2.1', '1.1'), 1)
        self.assertEqual(self.compareVersion('1.1', '1.1'), 0)
        self.assertEqual(self.compareVersion('1.1', '2.1'), -1)
        self.assertEqual(self.compareVersion('1', '1.1'), -1)
        self.assertEqual(self.compareVersion('1.0', '1'), 0)

    def partition(self, s):
        ''' https://oj.leetcode.com/problems/palindrome-partitioning/
        '''
        result = []

        def dfs(cur_idx, cur_result):
            if cur_idx == len(s):
                result.append(cur_result[:])
                return

            for i in range(cur_idx, len(s)):
                cur_str = s[cur_idx:i+1]
                if is_palindrome(cur_str):
                    cur_result.append(cur_str)
                    dfs(i+1, cur_result)
                    cur_result.pop()

        dfs(0, [])
        return result

    def test_partition(self):
        s = 'aab'
        rv = self.partition(s)
        self.assertIn(['a', 'a', 'b'], rv)
        self.assertIn(['aa', 'b'], rv)
        self.assertEqual(2, len(rv))

    def titleToNumber(self, s):
        '''https://oj.leetcode.com/problems/excel-sheet-column-number/
        '''
        ascii_table = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        result = 0
        p = 0
        for l in s[::-1]:
            idx = ascii_table.index(l) + 1
            result += idx * (26 ** p)
            p += 1
        return result

    def test_titleToNumber(self):
        self.assertEqual(self.titleToNumber('Z'), 26)
        self.assertEqual(self.titleToNumber('AA'), 27)

    def trailingZeroes(self, n):
        ''' https://oj.leetcode.com/problems/factorial-trailing-zeroes/

        1. 0 的数量取决于 2 和 5 的数量，5 的数量又比 2 少
        2. 25 这种又包含两个 5 所以需要一直除知道 n 小于 5
        '''
        count_5 = 0

        while n:
            c = n / 5
            count_5 += c
            n = c
        return count_5

    def test_trailingZeroes(self):
        self.assertEqual(self.trailingZeroes(0), 0)
        self.assertEqual(self.trailingZeroes(1), 0)
        self.assertEqual(self.trailingZeroes(10), 2)

    def findPeakElement(self, num):
        ''' https://oj.leetcode.com/problems/find-peak-element/
        '''
        idx = 0
        size_of_num = len(num)

        if not size_of_num:
            return None

        if size_of_num == 1:
            return 0

        while idx < size_of_num:
            if idx == 0:
                if num[idx] > num[idx+1]:
                    return idx
            elif idx == size_of_num - 1:
                if num[idx] > num[idx-1]:
                    return idx
            else:
                if num[idx] > num[idx-1] and num[idx] > num[idx+1]:
                    return idx
                if num[idx] > num[idx+1]:
                    idx += 1
            idx += 1
        return None

    def test_findPeakElement(self):
        num = [1, 2, 3, 1]
        self.assertEqual(self.findPeakElement(num), 2)

    def ladderLength(self, start, end, dict):
        ''' https://oj.leetcode.com/problems/word-ladder/
        '''

        def get_next_words(src):
            rv = []
            table = 'abcdefghijklmnopqrstuvwxyz'

            for idx, c in enumerate(src):
                for t in table:
                    if t == c:
                        continue
                    dst = "%s%s%s" % (src[:idx], t, src[idx+1:])
                    rv.append(dst)
            return rv

        cur_stack = [start]
        count = 1
        while cur_stack:
            next_stack = []
            for src in cur_stack:
                next_words = get_next_words(src)
                for word in next_words:
                    if word == end:
                        return count + 1
                    if word not in dict:
                        continue
                    dict.remove(word)
                    next_stack.append(word)

            if not next_stack:
                return 0
            cur_stack = next_stack
            count += 1

        return 0

    def test_ladderLength(self):
        start = 'hit'
        end = 'cog'
        words = set(["hot","dot","dog","lot","log"])
        self.assertEqual(self.ladderLength(start, end, words), 5)

if __name__ == "__main__":
    unittest.main()
