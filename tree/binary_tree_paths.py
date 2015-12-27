# -*- coding: utf-8 -*-


class Solution(object):

    def get_paths(self, node):
        '''
        '''
        if not node:
            return []

        if not node.left and not node.right:
            return [[node.val]]

        paths = []
        paths.extend(self.get_paths(node.left))
        paths.extend(self.get_paths(node.right))
        return [[node.val] + path for path in paths]

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        paths = self.get_paths(root)

        ret = []
        for path in paths:
            ret.append("->".join([str(val) for val in path]))
        return ret
