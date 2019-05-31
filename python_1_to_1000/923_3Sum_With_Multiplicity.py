_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/3sum-with-multiplicity/
# Given an integer array A, and an integer target, return the number of tuples i, j, k  such that i < j < k
# and A[i] + A[j] + A[k] == target.
# As the answer can be very large, return it modulo 10^9 + 7.

# Count the frequency of each number in A. For each pair of numbers, determine the other number required for the sum
# to equal the target. Reject cases when the other number is outside the possible range or any count is zero.
# If all numbers are the same, add to the result the count of combinations of 3 indices with that number.
# If the 2 numbers in the pair are the same, add to the result the count of combinations of 2 indices with that
# number times the count of other.
# If other > med, add all combinations of the 3 numbers. These are only added to the result when in order to avoid
# double counting.
# Time - O(n + k**2) where k is the range of values of A
# Space - O(k)

class Solution:
    def threeSumMulti(self, A, target):
        """
        :type A: List[int]
        :type target: int
        :rtype: int
        """
        counts = [0] * 101
        for num in A:
            counts[num] += 1

        result = 0

        for small, small_count in enumerate(counts):
            if small_count == 0:
                continue

            for med, med_count in enumerate(counts[small:], small):
                if med_count == 0:
                    continue

                other = target - small - med
                if other < 0 or other > 100 or counts[other] == 0:
                    continue
                other_count = counts[other]

                if small == med == other:
                    result += small_count * (small_count - 1) * (small_count - 2) // 6
                elif small == med:          # exactly 2 numbers are the same
                    result += small_count * (small_count - 1) * other_count // 2
                elif other > med:           # add if in order (med is always > small)
                    result += small_count * med_count * other_count

        return result % (10 ** 9 + 7)