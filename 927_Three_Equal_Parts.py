_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/three-equal-parts/
# Given an array A of 0s and 1s, divide the array into 3 non-empty parts such that all of these parts represent the
# same binary value.
# If it is possible, return any [i, j] with i+1 < j, such that:
# A[0], A[1], ..., A[i] is the first part;
# A[i+1], A[i+2], ..., A[j-1] is the second part, and
# A[j], A[j+1], ..., A[A.length - 1] is the third part.
# All three parts have equal binary value.
# If it is not possible, return [-1, -1].
# Note that the entire part is used when considering what binary value it represents.
# For example, [1,1,0] represents 6 in decimal, not 3.
# Also, leading zeros are allowed, so [0,1,1] and [1,1] represent the same value.

# The number of set bits must be divisible by 3. Find the start and end indices containing one_count // 3 set bits.
# Check that the second and third parts with the first bit set and the same length as the first part are identical.
# Find the trailing zeros from the third part and extend the ends of the first and second parts accordingly.
# Check that the parts do not overlap. There may be additional leading zeros.
# Time - O(n)
# Space - O(1)

class Solution:
    def threeEqualParts(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        one_count = sum(A)
        if one_count == 0:              # all zeros, split anywhere
            return [0, 2]

        ones_per_part, remainder = divmod(one_count, 3)
        if remainder != 0:              # cannot divide set bits into 3 equal groups
            return [-1, -1]

        first_start = 0
        while A[first_start] == 0:      # find first set bit
            first_start += 1

        first_end = first_start
        count = 1
        while count < ones_per_part:    # find ones_per_part-th set bit
            first_end += 1
            count += A[first_end]
        length = first_end - first_start + 1

        second_start = first_end + 1
        while A[second_start] == 0:     # first set bit of second part
            second_start += 1

        if A[first_start:first_end + 1] != A[second_start:second_start + length]:
            return [-1, -1]             # first and second part set bit patterns must be same

        third_start = second_start + length
        while A[third_start] == 0:
            third_start += 1

        if A[first_start:first_end + 1] != A[third_start:third_start + length]:
            return [-1, -1]

        trailing_zeros = len(A) - third_start - length  # extend 1st and 2nd parts by trailing_zeros from 3rd part
        first_end += trailing_zeros
        second_end = second_start + length - 1 + trailing_zeros

        if second_start < first_end + 1 or third_start < second_end + 1:    # cannot have overlap of parts
            return [-1, -1]

        return [first_end, second_end + 1]
