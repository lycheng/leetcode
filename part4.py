#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

__author__ = 'lycheng'
__email__ = "lycheng997@gmail.com"

from public import TreeNode

class Solution(object):
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        if not triangle:
            return 0

        for row in range(len(triangle) - 2, -1, -1):
            len_trigle_row = len(triangle[row])
            for column in range(0, len_trigle_row):
                cur_min_sum = min(triangle[row][column] + triangle[row+1][column],
                        triangle[row][column] + triangle[row+1][column+1])
                triangle[row][column] = cur_min_sum

        return triangle[0][0]

    def test_minimumTotal(self):
        src = [
                [2],
                [3,4],
                [6,5,7],
                [4,1,8,3]
        ]
        print self.minimumTotal(src)

    def hasPathSum(self, root, sum):
        if not root:
            return False

        need_sum = sum - root.val
        if need_sum == 0 and not root.left and not root.right:
            return True

        result = False
        if root.left:
            result = self.hasPathSum(root.left, need_sum)

        if root.right:
            result = result or self.hasPathSum(root.right, need_sum)

        return result

    def test_hasPathSum(self):

        root = TreeNode(5)
        root.left = TreeNode(4)
        root.left.left = TreeNode(11)
        root.left.left.left = TreeNode(7)
        root.left.left.right = TreeNode(2)
        root.right = TreeNode(8)
        root.right.left = TreeNode(13)
        root.right.right = TreeNode(4)
        root.right.right.right = TreeNode(1)

        print self.hasPathSum(root, 22)

    def sumNumbers(self, root):
        def get_all_nums(root):
            if not root:
                return ""
            if not root.left and not root.right:
                return [str(root.val)]

            rv = []
            if root.left:
                rv.extend(get_all_nums(root.left))
            if root.right:
                rv.extend(get_all_nums(root.right))
            rv = [str(root.val) + num for num in rv]
            return rv

        nums = get_all_nums(root)
        return sum([int(num) for num in nums])

    def test_sumNumbers(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        print self.sumNumbers(root)

    def restoreIpAddresses(self, s):
        def is_valid_num(num):
            return num and str(int(num)) == num

        rv = []
        for first in range(1, 4):
            first_num = s[0:first]
            if not is_valid_num(first_num):
                continue
            for second in range(first+1, first+4):
                second_num = s[first:second]
                if not is_valid_num(second_num):
                    continue

                for third in range(second+1, second+4):
                    third_num = s[second:third]
                    if not is_valid_num(third_num):
                        continue

                    four_num = s[third:]
                    if not is_valid_num(four_num):
                        continue

                    nums = [first_num, second_num, third_num, four_num]
                    if not all([num and int(num) <= 255 for num in nums]):
                        continue
                    ip = ".".join(nums)
                    rv.append(ip)

        return rv


    def test_restoreIpAddresses(self):
        print self.restoreIpAddresses('25525511135')
        print self.restoreIpAddresses('8888')
        print self.restoreIpAddresses('010010')


if __name__ == "__main__":
    so = Solution()
    # so.test_minimumTotal()
    # so.test_hasPathSum()
    # so.test_sumNumbers()
    so.test_restoreIpAddresses()
