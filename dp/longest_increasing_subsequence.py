# -*- coding: utf-8 -*-


class Solution(object):

    def lengthOfLIS_n2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_nums = len(nums)
        max_length = [1] * len_nums

        result = 0
        for i in range(len_nums):
            for j in range(i):
                if nums[i] <= nums[j]:
                    continue
                max_length[i] = max(max_length[i], max_length[j]+1)
                if max_length[i] > result:
                    result = max_length[i]
        return result

    def lengthOfLIS_nlogn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pass
