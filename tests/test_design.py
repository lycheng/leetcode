# -*- coding: utf-8 -*-

import unittest

from design import lru, min_stack


class TestDesign(unittest.TestCase):

    def test_lru(self):
        obj = lru.LRUCache(3)
        obj.set(1, 1)
        obj.set(2, 2)
        obj.set(3, 3)
        obj.set(4, 4)
        self.assertEqual(obj.get(4), 4)
        self.assertEqual(obj.get(3), 3)
        obj.set(5, 5)

        self.assertEqual(obj.get(1), -1)

    def test_lru_with_ordereddict(self):
        obj = lru.LRUCacheWithOrderedDict(3)
        obj.set(1, 1)
        obj.set(2, 2)
        obj.set(3, 3)
        obj.set(4, 4)
        self.assertEqual(obj.get(4), 4)
        self.assertEqual(obj.get(3), 3)
        obj.set(5, 5)

        self.assertEqual(obj.get(1), -1)

    def test_min_stack(self):
        s = min_stack.MinStack()

        s.push(512)
        s.push(-1024)
        s.push(-1024)
        s.push(512)
        s.pop()
        self.assertEqual(s.getMin(), -1024)
        s.pop()
        self.assertEqual(s.getMin(), -1024)
        s.pop()
        self.assertEqual(s.getMin(), 512)

    def test_queue(self):
        from design import queue
        q = queue.Queue()
        self.assertTrue(q.empty())

        q.push(1)
        q.push(2)
        q.push(3)

        self.assertEqual(q.peek(), 1)
        q.pop()
        self.assertEqual(q.peek(), 2)
        self.assertFalse(q.empty())
