#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

__author__ = 'lycheng'
__email__ = "lycheng997@gmail.com"

from public import linked_to_list, list_to_linked, ListNode, TreeNode

import unittest

class Solution(unittest.TestCase):

    def rotate(self, matrix):

        n = len(matrix)

        for i in range(n):
            for j in range(n):
                if i + j >= n -1:
                    continue
                matrix[i][j], matrix[n-1-j][n-1-i] = \
                        matrix[n-1-j][n-1-i], matrix[i][j]

        for i in range(n/2):
            matrix[i], matrix[n-1-i] = matrix[n-1-i], matrix[i]

        return matrix


    def test_rotate(self):
        matrix = [
            [1, 2],
            [3, 4]
        ]
        self.assertEqual(self.rotate(matrix), [[3, 1], [4, 2]])

        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]
        self.assertEqual(self.rotate(matrix), [[7, 4, 1], [8, 5, 2],[9, 6, 3]])

    def deleteDuplicates(self, head):
        if not head:
            return head

        new_head = ListNode(-1)
        new_head.next = head

        pre = new_head
        now = head

        while now and now.next:
            if now.next.val == now.val:
                while now.next and now.val == now.next.val:
                    now = now.next
                pre.next = now.next
            else:
                pre = now
            now = now.next

        return new_head.next

    def test_deleteDuplicates(self):
        src = [1, 1, 2, 3]
        root = list_to_linked(src)
        head = self.deleteDuplicates(root)
        self.assertEqual(linked_to_list(head), [2, 3])

    def isValidBST(self, root):
        def helper(root, min_val, max_val):
            if not root:
                return True

            if root.val >= max_val or root.val <= min_val:
                return False

            return helper(root.left, min_val, root.val) and helper(root.right, root.val, max_val)


        if not root:
            return True

        min_val = -999999999999
        max_val = -min_val

        return helper(root, min_val, max_val)

    def test_isValidBST(self):

        root = TreeNode(8)
        root.left = TreeNode(3)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(6)
        root.left.right.left = TreeNode(4)
        root.left.right.right = TreeNode(7)
        root.right = TreeNode(10)
        root.right.right = TreeNode(14)
        root.right.right.left = TreeNode(13)

        self.assertTrue(self.isValidBST(root))

    def postorderTraversal(self, root):
        rv = []
        if not root:
            return rv

        rv.extend(self.postorderTraversal(root.left))
        rv.extend(self.postorderTraversal(root.right))
        rv.append(root.val)

        return rv

    def test_postorderTraversal(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.left = TreeNode(3)

        self.assertEqual(self.postorderTraversal(root), [3, 2, 1])

    def candy(self, ratings):
        len_ratings = len(ratings)
        if len_ratings == 1:
            return 1

        candy_list = [1] * len_ratings

        if ratings[0] > ratings[1]:
            candy_list[0] = 2

        for i in range(1, len_ratings):
            if ratings[i] > ratings[i-1] and candy_list[i-1] >= candy_list[i]:
                candy_list[i] = candy_list[i-1] + 1

        for i in reversed(range(1, len_ratings)):
            if ratings[i-1] > ratings[i] and candy_list[i-1] <= candy_list[i]:
                candy_list[i-1] = candy_list[i] + 1

        return sum(candy_list)

    def test_candy(self):
        ratings = [1, 2, 3]
        self.assertEqual(6, self.candy(ratings))


        ratings = [5, 3, 1]
        self.assertEqual(6, self.candy(ratings))

    def searchMatrix(self, matrix, target):
        len_rows = len(matrix)
        for row in range(len_rows):
            if target < matrix[row][0]:
                return False
            if target > matrix[row][-1]:
                continue
            return target in matrix[row]

        return False

    def generateMatrix(self, n):
        def helper(num, x, y, matrix):
            if x >= n or y >= n or matrix[x][y]:
                return
            src_x, src_y = x, y
            matrix[x][y] = num
            num = num + 1

            for j in range(y+1, n):
                if matrix[x][j]:
                    j = j - 1
                    break
                matrix[x][j] = num
                num += 1
            y = j

            for i in range(x+1, n):
                if matrix[i][y]:
                    i = i - 1
                    break
                matrix[i][y] = num
                num += 1
            x = i

            for j in range(y-1, -1, -1):
                if matrix[x][j]:
                    j = j + 1
                    break
                matrix[x][j] = num
                num += 1
            y = j

            for i in range(x-1, -1, -1):
                if matrix[i][y]:
                    i = i + 1
                    break
                matrix[i][y] = num
                num += 1
            x = i

            if num > n ** 2:
                return
            helper(num, src_x+1, src_y+1, matrix)

        if not n:
            return []
        if n == 1:
            return [[1]]
        matrix = [[0] * n for i in range(n)]

        helper(1, 0, 0, matrix)
        return matrix

    def test_generateMatrix(self):
        self.assertEqual(self.generateMatrix(1), [[1]])
        self.assertEqual(self.generateMatrix(2), [[1, 2], [4, 3]])

    def detectCycle(self, head):
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

    def test_detectCycle(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        head.next.next.next.next = ListNode(5)
        head.next.next.next.next.next = ListNode(6)
        head.next.next.next.next.next.next = head.next.next
        self.assertEqual(self.detectCycle(head).val, 3)

    def getRow(self, rowIndex):
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]

        row = [0] * (rowIndex + 1)
        row[0], row[1] = 1, 1
        cur_item = 2
        while cur_item <= rowIndex:
            for i in xrange(cur_item, 0, -1):
                row[i] = row[i] + row[i-1]
            cur_item += 1

        return row[:(rowIndex+1)]

    def test_getRow(self):
        self.assertEqual([1, 3, 3, 1], self.getRow(3))
        self.assertEqual([1, 4, 6, 4, 1], self.getRow(4))

    def search(self, A, target):
        l, r = 0, len(A) - 1

        while l <= r:
            mid = (l + r) / 2
            if target == A[mid]:
                return mid

            if A[mid] >= A[l]:
                if A[l] <= target and A[mid] >= target:
                    r = mid - 1
                else:
                    l = mid + 1
            else:

                if A[mid] > target or target >= A[l]:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1

    def test_search(self):
        src = [4, 5, 6, 7, 0, 1, 2]
        self.assertEqual(self.search(src, 0), 4)


if __name__ == "__main__":
    unittest.main()
