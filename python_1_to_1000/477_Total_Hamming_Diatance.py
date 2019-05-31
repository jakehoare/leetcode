_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/total-hamming-distance/
# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
# Now your job is to find the total Hamming distance between all pairs of the given numbers.

# For each of the 32 bits, count how many nums have that bit set. Add to total hamming distance count of pairs from
# nums where one num has bit set and one num soes not have bit set.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        hamming = 0

        for bit in range(32):
            set_bits = 0  # count of nums with this bit set
            for num in nums:
                set_bits += (num >> bit) & 1

            hamming += (n - set_bits) * set_bits

        return hamming