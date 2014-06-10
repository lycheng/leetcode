#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

__author__ = 'lycheng'
__email__ = "lycheng997@gmail.com"

from public import TreeNode

class Solution(object):

    def pathSum(self, root, sum):

        self.result = []

        def helper(root, target, rv):
            if not root:
                return []

            next_target = target - root.val
            cur_rv = rv[:]
            cur_rv.append(root.val)
            if next_target == 0 and not root.left and not root.right:
                self.result.append(cur_rv)
                return

            if root.left:
                helper(root.left, next_target, cur_rv[:])
            if root.right:
                helper(root.right, next_target, cur_rv[:])

        helper(root, sum, [])
        return self.result

    def test_pathSum(self):
        root = TreeNode(5)
        root.left = TreeNode(4)
        root.right = TreeNode(8)
        root.left.left = TreeNode(11)
        root.left.left.left = TreeNode(7)
        root.left.left.right = TreeNode(2)
        root.right.left = TreeNode(13)
        root.right.right = TreeNode(4)
        root.right.right.left = TreeNode(5)
        root.right.right.right = TreeNode(1)

        print self.pathSum(root, 22)


if __name__ == "__main__":
    so = Solution()
    so.test_pathSum()
