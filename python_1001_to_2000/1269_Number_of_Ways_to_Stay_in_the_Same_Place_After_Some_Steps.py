_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/
# You have a pointer at index 0 in an array of size arrLen.
# At each step, you can move 1 position to the left, 1 position to the right in the array or stay in the same place.
# The pointer should not be placed outside the array at any time.
# Given two integers steps and arrLen,
# return the number of ways such that your pointer still at index 0 after exactly steps steps.
# Since the answer may be too large, return it modulo 10^9 + 7.

# Count the number of way to reach each index.
# Do not count all indices of the array, since initially most are zero and if the array is much longer than
# the number of steps, we cannot return to index zero from all indices.
# For each step, iterate over the existing array elements that can reach index zero in the remaining steps.
# For x ways to reach index i, add x to the number of ways to reach indices i - 1, i and i + 1 on the next step,
# provided those new indices are within the bounds of the array.
# Time - O(n**2) for n steps
# Space - O(n)

class Solution(object):
    def numWays(self, steps, arrLen):
        """
        :type steps: int
        :type arrLen: int
        :rtype: int
        """
        i_to_count = [1]            # i_to_count[i] is the number of ways to reach index i

        for step in range(steps):
            new_i_to_count = [0] * (len(i_to_count) + 1)    # extend length by 1 since we may move +1 index

            for i, count in enumerate(i_to_count[:steps - step + 1]):   # only consider indices where we can move
                if i + 1 < arrLen:                                      # back to index 0 in remaining steps
                    new_i_to_count[i + 1] += count
                new_i_to_count[i] += count
                if i - 1 >= 0:
                    new_i_to_count[i - 1] += count

            i_to_count = new_i_to_count

        return i_to_count[0] % (10 ** 9 + 7)
