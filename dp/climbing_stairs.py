# -*- coding: utf-8 -*-


class Solution(object):
    ''' https://leetcode.com/problems/climbing-stairs/
    '''

    def climbStairs(self, n):
        if n in [0, 1, 2]:
            return n

        two_step_solution = 1
        one_step_solution = 2
        cur_step = 2
        cur_solution = 0

        while cur_step < n:
            cur_solution = two_step_solution + one_step_solution
            two_step_solution = one_step_solution
            one_step_solution = cur_solution
            cur_step += 1

        return cur_solution
