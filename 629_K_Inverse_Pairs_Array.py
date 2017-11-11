_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/k-inverse-pairs-array/
# Given two integers n and k, find how many different arrays consist of numbers from 1 to n such that there are
# exactly k inverse pairs.
# We define an inverse pair as following: For ith and jth element in the array, if i < j and a[i] > a[j] then it's
# an inverse pair; Otherwise, it's not.
# Since the answer may be very large, the answer should be modulo 10**9 + 7.

# Given the counts of arrangements with i inverse pairs of integers up to n, where i <= k, find the counts for n + 1.
# Store the cumulative sums of arrangements by number of inverse pairs.
# We can put n + 1 at any position in the array to increase the number of arrangements by anywhere from 0 to n for
# all existing arrangements. To find the cumulative count for n + 1, nb_pairs, add the cumulative count for n + 1,
# nb_pairs - 1 to the cumulative count for n, nb_pairs. If nb_pairs cannot be reached by adding n pairs, subtract
# these from cumulative sum.

# Time - O(n * k)
# Space - O(k)

class Solution(object):
    def kInversePairs(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if k == 0:
            return 1

        MODULO = 10 ** 9 + 7

        # inverse_pairs[i] is nb arrangements for current num with <= i inverse pairs
        inverse_pairs = [0 for _ in range(k + 1)]

        for num in range(1, n + 1):  # increment num from 1 up to n

            next_inverse_pairs = [1]  # always one sorted arrangement with no inverse pairs

            for nb_pairs in range(1, k + 1):

                next_inverse_pairs.append(next_inverse_pairs[-1])  # cumulative sum
                next_inverse_pairs[-1] += inverse_pairs[nb_pairs]  # add arrangements for num-1 up to nb_pairs
                if nb_pairs - num >= 0:  # can only increase by num-1 pairs
                    next_inverse_pairs[-1] -= inverse_pairs[nb_pairs - num]
                next_inverse_pairs[-1] %= MODULO

            inverse_pairs = next_inverse_pairs

        return (inverse_pairs[-1] - inverse_pairs[-2]) % MODULO  # mod is always positive