# -*- coding: utf-8 -*-

''' https://leetcode.com/problems/lru-cache/
'''

from collections import OrderedDict


class ListNode(object):
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache(object):
    ''' TLE
    '''
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.head = ListNode(None)
        self.tail = ListNode(None, self.head)
        self.head.next = self.tail
        self.key_index = {}

    def __set(self, node):
        ''' append the node to the head, del the node if the key exists
        '''
        key, value = node.val
        self.key_index[key] = node
        self.__append_head(node)
        self.__remove_tail()

    def __append_head(self, node):
        ''' append the node to the head
        '''
        head_node = self.head.next
        self.head.next = node
        node.prev = self.head
        head_node.prev = node
        node.next = head_node

        self.size += 1

    def __remove_tail(self):
        ''' remove tail nodes if size > capacity
        '''
        if self.size <= self.capacity:
            return

        while self.size > self.capacity:
            tail_node = self.tail.prev
            if not tail_node.val:  # head
                return
            self.__del_node(tail_node.val[0])

    def __del_node(self, key):
        ''' del a node and remove the key in key_index
        '''
        node = self.key_index[key]
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        del node
        self.key_index.pop(key)
        self.size -= 1

    def __get_val(self, key):
        ''' get a val
        '''
        ptr = self.head.next
        while ptr.next:
            if ptr.val[0] == key:
                return ptr.val[1]
            ptr = ptr.next

    def get(self, key):
        if key not in self.key_index:
            return -1

        key, val = self.key_index[key].val
        # val = self.__get_val(key)
        self.__del_node(key)
        node = ListNode((key, val))
        self.__set(node)

        return val

    def set(self, key, value):

        if key in self.key_index:
            self.__del_node(key)

        node = ListNode((key, value))
        self.__set(node)


class LRUCacheWithOrderedDict(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = OrderedDict()

    def get(self, key):
        '''

        :param key: string
        '''
        if key not in self.data:
            return -1
        value = self.data.pop(key)
        self.data[key] = value
        return value

    def set(self, key, value):
        '''

        :param key: string
        :param value: string or something
        '''
        if key in self.data:
            self.data.pop(key)
        elif len(self.data) == self.capacity:
            self.data.popitem(last=False)
        self.data[key] = value
