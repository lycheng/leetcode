#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

__author__ = 'lycheng'
__email__ = "lycheng997@gmail.com"

from public import TreeNode

class BSTIterator:
    ''' https://oj.leetcode.com/problems/binary-search-tree-iterator/
    '''

    def __init__(self, root):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def hasNext(self):
        return len(self.stack) > 0

    def next(self):
        if not self.hasNext():
            return None
        node = self.stack.pop()
        rv = node.val
        node = node.right
        while node:
            self.stack.append(node)
            node = node.left

        return rv

if __name__ == "__main__":
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)

    bst_iter = BSTIterator(root)

    assert bst_iter.next() == 1
    assert bst_iter.next() == 2
    assert bst_iter.next() == 3
    assert bst_iter.hasNext() == False

