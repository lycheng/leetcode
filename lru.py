#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

__author__ = 'lycheng'
__email__ = "lycheng997@gmail.com"

class ListNode(object):
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache(object):
    # @param capacity, an integer
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
            if tail_node.val == None: # head
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

    def print_val(self):
        head_node = self.head.next
        print "---"
        while head_node and head_node.val:
            print head_node.val
            head_node = head_node.next

        print "---"

    # @return an integer
    def get(self, key):
        if key not in self.key_index:
            return -1

        key, val = self.key_index[key].val
        self.__del_node(key)
        node = ListNode((key, val))
        self.__set(node)

        return val

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.key_index:
            self.__del_node(key)

        node = ListNode((key, value))
        self.__set(node)

if __name__ == "__main__":
    #2,[set(2,1),set(2,2),get(2),set(1,1),set(4,1),get(2)]
    #3,[set(1,1),set(2,2),set(3,3),set(4,4),get(4),get(3),get(2),get(1),set(5,5),get(1),get(2),get(3),get(4),get(5)]

    obj = LRUCache(3)
    obj.set(1, 1)
    obj.set(2, 2)
    obj.set(3, 3)
    obj.set(4, 4)
    r = obj.get(4)
    print "get val: %d" % r
    r = obj.get(3)
    print "get val: %d" % r
    r = obj.get(2)
    print "get val: %d" % r
    r = obj.get(1)
    print "get val: %d" % r
    obj.set(5, 5)
    r = obj.get(1)
    print "get val: %d" % r
    r = obj.get(2)
    print "get val: %d" % r
    r = obj.get(3)
    print "get val: %d" % r
    r = obj.get(4)
    print "get val: %d" % r
    r = obj.get(5)
    print "get val: %d" % r
