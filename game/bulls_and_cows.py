#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

__author__ = 'lycheng'
__email__ = "lycheng997@gmail.com"


class Solution(object):

    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """

        bulls = 0
        cows = 0
        char_count = dict()
        for idx, char in enumerate(secret):
            if char not in char_count:
                char_count[char] = 0

            if char == guess[idx]:
                bulls += 1
            else:
                char_count[char] += 1

        for idx, char in enumerate(guess):
            if char_count.get(char, 0) <= 0 or char == secret[idx]:
                continue
            char_count[char] -= 1
            cows += 1
        return "%dA%dB" % (bulls, cows)
