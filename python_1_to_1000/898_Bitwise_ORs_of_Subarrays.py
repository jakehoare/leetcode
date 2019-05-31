_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/bitwise-ors-of-subarrays/
# We have an array A of non-negative integers.
# For every (contiguous) subarray B = [A[i], A[i+1], ..., A[j]] (with i <= j), we take the bitwise OR of all the
# elements in B, obtaining a result A[i] | A[i+1] | ... | A[j].
# Return the number of possible results.
# Results that occur more than once are only counted once in the final answer.

# Create sets of all numbers that can be created by OR and all numbers that can be created using the subarray ending
# at the current index. For each index i, the results for the subarray ending at i are the OR of all previous results
# and A[i], and A[i] alone. Update all the results with the results from each index.
# Time - O(n) since the length of subarray_or is at most 30 (the number of bits in any num) because each longer
# subarray ending at a given index covers al least all the bits covered by a shorter subarray.
# Space - O(n)

class Solution(object):
    def subarrayBitwiseORs(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        all_or, subarray_or = set(), set()

        for num in A:
            new_or = {num | x for x in subarray_or}
            new_or.add(num)

            all_or |= new_or
            subarray_or = new_or

        return len(all_or)
