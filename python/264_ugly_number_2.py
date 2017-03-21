'''
An ugly number must be multiplied by either primes from a smaller ugly number.
Use three pointers to save the least possible candidate.
'''
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        primes = [2, 3, 5]
        ugly = [1 for i in xrange(n)]
        index = [0, 0, 0]
        for i in xrange(1, n):
            minNum = float('inf')
            for j in xrange(3):
                # find smallest uglynum
                minNum = min(minNum, primes[j]*ugly[index[j]])
            for j in xrange(3):
                # remove duplicate candidate
                if primes[j]*ugly[index[j]] == minNum:
                    index[j] += 1
            ugly[i] = minNum
        return ugly[-1]
