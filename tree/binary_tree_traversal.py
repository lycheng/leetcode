# -*- coding: utf-8 -*-


class Solution(object):

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        if not root:
            return ret

        ret.extend(self.inorderTraversal(root.left))
        ret.append(root.val)
        ret.extend(self.inorderTraversal(root.right))
        return ret

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        ret = []
        if not root:
            return ret
        ret.append(root.val)
        ret.extend(self.preorderTraversal(root.left))
        ret.extend(self.preorderTraversal(root.right))
        return ret

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        if not root:
            return ret
        ret.extend(self.postorderTraversal(root.left))
        ret.extend(self.postorderTraversal(root.right))
        ret.append(root.val)
        return ret
