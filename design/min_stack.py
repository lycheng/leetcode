# -*- coding: utf-8 -*-

__author__ = 'lycheng'
__email__ = "lycheng997@gmail.com"


class MinStack(object):
    ''' https://leetcode.com/problems/min-stack/
    '''

    def __init__(self):
        self.items = []
        self.min_items = []

    def push(self, x):
        '''
        @param x, an integer
        @return an integer
        '''
        if not self.min_items or self.min_items[-1] >= x:
            self.min_items.append(x)
        self.items.append(x)

    def pop(self):
        '''
        @return nothing
        '''
        item = self.items.pop()
        if self.min_items and item == self.min_items[-1]:
            self.min_items.pop()

    def top(self):
        '''
        @return an integer
        '''
        if self.items:
            return self.items[-1]
        return None

    def getMin(self):
        '''
        @return an integer
        '''
        if self.min_items:
            return self.min_items[-1]
        return None
