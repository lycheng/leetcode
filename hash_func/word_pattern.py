# -*- coding: utf-8 -*-

__author__ = 'lycheng'
__email__ = "lycheng997@gmail.com"


class Solution(object):

    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split(" ")
        if len(pattern) != len(words):
            return False

        word_map = {}
        pattern_map = {}
        for idx, word in enumerate(words):
            p = pattern[idx]
            if p not in pattern_map and word not in word_map:
                pattern_map[p] = word
                word_map[word] = p
                continue

            if pattern_map.get(p) != word or word_map.get(word) != p:
                return False

        return True
