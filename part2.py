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

