# -*- coding: utf-8 -*-


class Solution(object):

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) < 3:
            return max(nums)

        last_rob = [nums[0], max(nums[:2])]
        for i in range(2, len(nums)):
            last_rob.append(max(nums[i]+last_rob[i-2], last_rob[i-1]))
        return last_rob[-1]
