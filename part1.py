#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

__author__ = 'lycheng'
__email__ = "lycheng997@gmail.com"

class Solution(object):
    def reverseWords(self, s):
        ''' reverseWords
        @param s, a string
        @return a string
        '''
        s = ' '.join(s.split())  # 分割出一个个单词出来
        words = s.split(' ')
        words = [word[::-1] for word in words]
        return " ".join(words)[::-1]

    def singleNumber(self, li):
        ''' return the single num in array
        @param A, a list of integer
        @return an integer
        '''
        rv = reduce(lambda x, y: x ^ y, li)
        return rv

    def maxDepth(self, root):
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def isSameTree(self, p, q):
        '''
        '''
        if not p and not q:
            return True

        if p and q:
            if p.val != q.val:
                return False
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        return False

    def reverse(self, x):
        ''' reverse number
        '''

        if x < 0:
            m = -1
        else:
            m = 1
        x = str(x * m)[::-1]
        return m * int(x)



def run():
    o = Solution()
    # print o.reverseWords("    the sky is       blue")
    o.singleNumber([1, 2, 3, 4, 5, 3, 2, 1, 4])


if __name__ == "__main__":
    run()
