_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/factor-combinations/
# Numbers can be regarded as product of its factors. For example,
# Write a function that takes an integer n and return all possible combinations of its factors.

# Recursive helper function returns all combinations of factors of n starting from trial factor, where partial is the
# list of existing factors.  Whenever trial is a factor add a new result and recurse without this factor.
# Alternatively, iterative version same except stack replaces recursive calls.

import time

class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        return self.factorise(n, 2, [], [])

    def factorise(self, n, trial, partial, factors):

        while trial * trial <= n:       # if trial**2 > n then have already found all factors

            if n % trial == 0:                                  # trial is a factor
                factors.append(partial + [n//trial, trial])     # append this result
                self.factorise(n//trial, trial, partial + [trial], factors) # try and factorise again with trial
            trial += 1

        return factors


class Solution2(object):
    def getFactors(self, n):
        stack = [(n, 2, [])]        # tuples of number to factorise, trial factor, list of previous factors
        factors = []

        while stack:
            num, trial, partial = stack.pop()

            while trial * trial <= num:     # as per recursive with push to stack replacing function call

                if num % trial == 0:
                    factors.append(partial + [num//trial, trial])
                    stack.append((num//trial, trial, partial + [trial]))
                trial += 1

        return factors

import matplotlib.pyplot as plt
import random
inputs = []
times = []
sol = Solution2()
i = 0
while i < 10000000:
    start = time.time()
    sol.getFactors(i)
    times.append(time.time()-start)
    inputs.append(i)
    i += random.randint(1,10000)
plt.plot(inputs, times, 'o')
plt.show()


