#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

__author__ = 'lycheng'
__email__ = "lycheng997@gmail.com"

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

    def __str__(self):
        return str(self.val)


def linked_to_list(head):
    ''' change linked list to list
    '''
    rv = []
    beg = head
    while beg:
        rv.append(beg.val)
        beg = beg.next
    return rv

def list_to_linked(li):
    if not li:
        return None

    head = ListNode(li[0])
    beg = head
    for index in range(1, len(li)):
        beg.next = ListNode(li[index])
        beg = beg.next

    return head
