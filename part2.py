#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

__author__ = 'lycheng'
__email__ = "lycheng997@gmail.com"

class Solution(object):

    def maxSubArray(self, A):
        rv = A[0]
        cur_sum = 0

        for num in A:
            if cur_sum < 0:
                cur_sum = num
            else:
                cur_sum += num
            if rv < cur_sum:
                rv = cur_sum

        return rv

    def removeElement(self, A, elem):
        index = 0
        for num in A:
            if num == elem:
                continue
            A[index] = num
            index += 1

        return index

    def twoSum(self, num, target):
        nums = sorted(num)

        left = 0
        right = len(num) - 1

        while left < right:
            cur_sum = nums[left] + nums[right]
            if cur_sum > target:
                right -= 1
                continue
            elif cur_sum < target:
                left += 1
                continue
            if cur_sum == target:
                break

        result = []
        for index in range(len(num)):
            if num[index] == nums[left]:
                result.append(index + 1)
            elif num[index] == nums[right]:
                result.append(index + 1)

            if len(result) == 2:
                break

        return tuple(result)

    def lengthOfLastWord(self, s):
        if not s:
            return 0

        length = 0
        s = ' '.join(s.split())  # 分割出一个个单词出来
        words = s.split(' ')
        if words:
            length = len(words[-1])
        return length

    def wordBreak(self, s, dict):
        if not s:
            return False

        perfix_words = [word for word in dict if s.startswith(word)]
        suffix_words = [word for word in dict if s.endswith(word)]

        for perfix_word in perfix_words:
            if perfix_word == s:
                return True
            for suffix_word in suffix_words:
                if perfix_word + suffix_word == s:
                    return True
                len_perfix_word = len(perfix_word)
                len_suffix_word = len(suffix_word)

                if len_perfix_word + len_suffix_word > len(s):
                    continue

                mid_word = s[len_perfix_word:len(s) - len_suffix_word]
                if self.wordBreak(mid_word, dict):
                    return True

        return False

# if __name__ == "__main__":

    # so = Solution()
    # s = "12345"
    # di = ['12', '3', '45']
    # print so.wordBreak(s, di)
