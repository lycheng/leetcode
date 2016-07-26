# -*- coding: utf-8 -*-

__author__ = 'lycheng'
__email__ = "lycheng997@gmail.com"


class Queue(object):
    ''' https://leetcode.com/problems/implement-queue-using-stacks/
    '''

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def __reverse_stack(self):
        s = []
        while len(self.stack) > 0:
            s.append(self.stack.pop())

        self.stack = s

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        self.__reverse_stack()
        self.stack.pop()
        self.__reverse_stack()

    def peek(self):
        """
        :rtype: int
        """
        self.__reverse_stack()
        result = self.stack[-1]
        self.__reverse_stack()
        return result

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.stack) == 0
