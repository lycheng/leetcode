#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

__author__ = 'lycheng'
__email__ = "lycheng997@gmail.com"

from public import ListNode, TreeNode
from public import list_to_linked, linked_to_list

import unittest
from string import ascii_lowercase

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

    def inorder_postorder_to_tree(self, inorder, postorder):
        def helper(inorder, postorder):
            if not inorder:
                return None
            root_val = postorder[-1]
            root = TreeNode(root_val)
            mid_idx = inorder.index(root_val)

            root.left = helper(inorder[:mid_idx], postorder[:mid_idx])
            root.right = helper(inorder[mid_idx+1:], postorder[mid_idx:-1])

            return root

        return helper(inorder, postorder)

    def preorder_inorder_to_tree(self, preorder, inorder):
        def helper(preorder, inorder):
            if not preorder:
                return None

            root_val = preorder[0]
            root = TreeNode(root_val)
            mid_idx = inorder.index(root_val)

            root.left = helper(preorder[1:mid_idx+1], inorder[:mid_idx])
            root.right = helper(preorder[1+mid_idx:], inorder[mid_idx+1:])
            return root

        return helper(preorder, inorder)

    def isPalindrome(self, s):
        def is_valid(c):
            if c >= 'a' and c <= 'z':
                return True
            if c >= '0' and c <= '9':
                return True
            return False

        if not s:
            return True
        s = s.lower().replace(' ', '')
        letters = [c for c in s if is_valid(c)]
        beg = 0
        end = len(letters) - 1

        while beg < end:
            if letters[beg] != letters[end]:
                return False
            beg += 1
            end -= 1

        return True

    def test_isPalindrome(self):
        self.assertTrue(self.isPalindrome('A man, a plan, a canal: Panama'))
        self.assertFalse(self.isPalindrome('race a car'))

    def countAndSay(self, n):
        if not n:
            return ""

        result = '1'
        for i in range(n-1):
            cur_result = ""
            cur_count = 0
            prev_num = result[0]
            for num in result:
                if prev_num == num:
                    cur_count += 1
                else:
                    cur_result += str(cur_count) + prev_num
                    cur_count = 1
                    prev_num = num

            cur_result += str(cur_count) + prev_num
            result = cur_result
        return result

    def test_countAndSay(self):
        self.assertEqual('11', self.countAndSay(2))
        self.assertEqual('21', self.countAndSay(3))
        self.assertEqual('1211', self.countAndSay(4))

    def is_num_Palindrome(self, x):
        if x < 0:
            return False

        di = 1
        while x / di >= 10:
            di *= 10

        while x:
            left = x / di
            right = x % 10
            if left != right:
                return False
            x = (x % di) / 10
            di /= 100
        return True

    def test_is_num_Palindrome(self):
        self.assertTrue(self.is_num_Palindrome(121))
        self.assertTrue(self.is_num_Palindrome(1221))
        self.assertTrue(self.is_num_Palindrome(1))



if __name__ == "__main__":
    unittest.main()
