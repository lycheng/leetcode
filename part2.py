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

    def plusOne(self, digits):
        if not digits:
            return []

        digits[-1] = digits[-1] + 1
        carry = 0

        for index in range(len(digits) - 1, -1, -1):
            digits[index] = digits[index] + carry
            if digits[index] >= 10:
                carry = 1
                digits[index] = digits[index] - 10
            else:
                carry = 0

        rv = digits
        if carry:
            rv = [1]
            rv.extend(digits)

        return rv

    def plusOne_I(self, digits):

        if not digits:
            return []

        num = int("".join([str(digit) for digit in digits]))
        num = num + 1
        return [int(digit) for digit in str(num)]

    def generate(self, numRows):
        if not numRows:
            return []

        rv = []
        rv.append([1])
        if numRows == 1:
            return rv

        rv.append([1, 1])
        if numRows == 2:
            return rv

        for row in range(2, numRows):
            cur_nums = [rv[-1][index] + rv[-1][index + 1] for index in range(0, row - 1)]
            cur_row = [1]
            cur_row.extend(cur_nums)
            cur_row.append(1)
            rv.append(cur_row)

        return rv


if __name__ == "__main__":
    so = Solution()
    print so.generate(3)
