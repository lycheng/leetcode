# -*- coding: utf-8 -*-


class Solution(object):

    def countPrimes(self, n):
        if n <= 2:
            return 0

        is_prime = [True] * n

        ret = 0
        for i in xrange(2, n):
            if not is_prime[i]:
                continue
            ret += 1
            for m in xrange(2, n):
                if i * m >= n:
                    continue
                is_prime[i*m] = False
        return ret
