_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/
# Given an array A of integers, return true if and only if we can partition the array into three non-empty parts
# with equal sums.
# Formally, we can partition the array if we can find indexes i+1 < j with (A[0] + A[1] + ... + A[i] ==
# A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1])

# Check if the total is divisible by 3. If so, iterate along the array counting the subarrays with sum of one third
# of the total sum.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def canThreePartsEqualSum(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        partition, remainder = divmod(sum(A), 3)
        if remainder != 0:
            return False

        subarray = 0                # sum of subarray
        partitions = 0              # number of partitions found

        for num in A:
            subarray += num
            if subarray == partition:
                partitions += 1
                subarray = 0        # reset the subarray sum

        return partitions >= 3      # ok if more than 3 partitions
