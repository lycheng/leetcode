#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

__author__ = 'lycheng'
__email__ = "lycheng997@gmail.com"

from public import ListNode, TreeNode
from public import list_to_linked, linked_to_list

import unittest

class Solution(unittest.TestCase):

    def zigzagLevelOrder(self, root):
        result = []
        if not root:
            return result

        left_to_right = 0
        result.append([root.val])
        cur_level = [root]
        next_level = []
        while cur_level:
            node = cur_level.pop(0)
            if node.left or node.right:
                next_level.append(node.left)
                next_level.append(node.right)

            if not cur_level:
                if not next_level:
                    break
                cur_level = [n for n in next_level if n]
                if left_to_right:
                    result.append([n.val for n in cur_level])
                else:
                    result.append([n.val for n in reversed(cur_level)])
                left_to_right = left_to_right ^ 1
                next_level = []

        return result

    def test_zigzagLevelOrder(self):
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)

        self.assertEqual([[3], [20, 9], [15, 7]], self.zigzagLevelOrder(root))

    def subsets(self, S):
        if not S:
            return []
        S = sorted(S)
        rv = [[]]
        len_s = len(S)
        def helper(idx, tmp):
            for i in range(idx, len_s):
                tmp.append(S[i])
                rv.append(tmp[:])
                if i < len_s - 1:
                    helper(i+1, tmp)
                tmp.pop()
        helper(0, [])
        return rv

    def test_subsets(self):
        rv = [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
        self.assertEqual(rv, self.subsets([1, 2, 3]))

    def subsetsWithDup(self, S):
        if not S:
            return []
        S = sorted(S)
        rv = [[]]
        len_s = len(S)
        def helper(idx, tmp):
            i = idx
            while i < len_s:
                tmp.append(S[i])
                rv.append(tmp[:])
                if i < len_s - 1:
                    helper(i+1, tmp)
                tmp.pop()
                while i < len_s - 1 and S[i] == S[i+1]:
                    i += 1
                i += 1
        helper(0, [])
        return rv

    def test_subsetsWithDup(self):
        rv = [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
        self.assertEqual(rv, self.subsetsWithDup([1, 2, 2]))

    def reverseBetween(self, head, m, n):
        if not head or not head.next:
            return head
        first = ListNode(-1)
        first.next = head
        prev = first
        # prev - m - ... - n
        for i in range(m-1):
            prev = prev.next

        p = prev.next
        q = p.next

        for i in range(n-m):
            r = q.next
            q.next = p
            if i == n - m - 1:
                prev.next.next = r
                prev.next = q
            p = q
            q = r

        return first.next

    def test_reverseBetween(self):
        li = list_to_linked([1, 2, 3, 4, 5, 6])
        head = self.reverseBetween(li, 1, 3)
        li = linked_to_list(head)
        exp = [3, 2, 1, 4, 5, 6]
        self.assertEqual(li, exp)

    def letterCombinations(self, digits):
        digit_map = {'0': "", '1': ' ', '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', \
                '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        rv = []
        def helper(idx, cur_set):
            if len(cur_set) == len(digits):
                rv.append(''.join(cur_set))
                return
            cur_digit = digits[idx]
            letters = digit_map[cur_digit]
            for i in letters:
                cur_set.append(i)
                helper(idx+1, cur_set)
                cur_set.pop()
        helper(0, [])
        return rv

    def test_letterCombinations(self):
        s = '23'
        rv = ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
        self.assertEqual(self.letterCombinations(s), rv)

    def longestConsecutive(self, num):
        if not num:
            return 0
        max_len = -1
        visited = {n:False for n in num}
        for n in num:
            if visited[n]:
                continue
            visited[n] = True
            cur_len = 1

            prev = n - 1
            while prev in visited:
                cur_len += 1
                visited[prev] = True
                prev -= 1

            next = n + 1
            while next in visited:
                cur_len += 1
                visited[next] = True
                next += 1

            if cur_len > max_len:
                max_len = cur_len

        return max_len

    def test_longestConsecutive(self):
        li = [100, 4, 200, 1, 3, 2]
        self.assertEqual(4, self.longestConsecutive(li))

        li = [1, 2, 0, 1]
        self.assertEqual(3, self.longestConsecutive(li))



if __name__ == "__main__":
    unittest.main()
