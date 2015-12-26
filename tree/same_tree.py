# -*- coding: utf-8 -*-


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True

        if p and q:
            if p.val != q.val:
                return False
            return self.isSameTree(p.left, q.left) and \
                self.isSameTree(p.right, q.right)

        return False
