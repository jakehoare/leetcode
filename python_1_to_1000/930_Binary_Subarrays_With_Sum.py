_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/binary-subarrays-with-sum/
# In an array A of 0s and 1s, how many non-empty subarrays have sum S?

# Iterate along A, counting the number of each prefix sum of A.
# For every prefix subarray, we can make a subarray of sum S with every other prefix subarray of sum running - S.
# Time - O(n)
# Space - O(n)

from collections import defaultdict

class Solution:
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        result = 0
        running = 0                             # prefix sum
        partials = defaultdict(int, {0: 1})     # map prefix sum to its count

        for i, a in enumerate(A):
            running += a
            result += partials[running - S]
            partials[running] += 1              # increment the count with this prefix sum

        return result