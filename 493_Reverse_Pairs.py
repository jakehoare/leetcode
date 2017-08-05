_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/reverse-pairs/
# Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].
# You need to return the number of important reverse pairs in the given array.

# Mergesort. Before merge, count reversed pairs in sorted left and right lists.
# Time - O(n log n)
# Space - O(n log n)

class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.pairs = 0

        def mergesort(nums):
            if len(nums) < 2:
                return nums

            mid = len(nums) // 2
            left = mergesort(nums[:mid])
            right = mergesort(nums[mid:])
            return merge(left, right)

        def merge(left, right):
            j = 0
            for num in left:
                while j < len(right) and num > 2 * right[j]:
                    j += 1
                self.pairs += j     # num is greater than right[j-1] and lower

            # return sorted(left + right) is faster than manual merge below
            merged = []
            i, j = 0, 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1

            return merged + left[i:] + right[j:]

        mergesort(nums)
        return self.pairs

