_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/
# Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 2**31.
# Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.

# Starting from prefix of 1st bit, create a set of all prefixes. For each prefix, check the set for another prefix
# that when xored together extend the max_xor by a bit.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mask = 0        # used to isolate the prefix bits of each num
        max_xor = 0     # current best result

        for bit in range(31, -1, -1):           # most significant bit first

            mask |= (1 << bit)                  # update mask with latest bit set
            prefixes = {mask & num for num in nums}
            target = max_xor | (1 << bit)       # xor of 2 prefixes with bit set

            for prefix in prefixes:             # if p ^ t = q then p ^ t ^ p = t = q ^ p
                if prefix ^ target in prefixes:
                    max_xor = target
                    break

        return max_xor

