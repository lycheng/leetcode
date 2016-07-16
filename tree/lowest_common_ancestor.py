# -*- coding: utf-8 -*-


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p.val < q.val:
            min_node = p
            max_node = q
        else:
            min_node = q
            max_node = p

        return self.find(root, min_node, max_node)

    def find(self, root, min_node, max_node):
        if min_node.val <= root.val <= max_node.val:
            return root

        if root.val > min_node.val:
            return self.find(root.left, min_node, max_node)
        else:
            return self.find(root.right, min_node, max_node)
