_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/wiggle-sort-ii/
# Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....
# You may assume all input has valid answer.

# Find the median (can be O(n) QuickSelect as per "215_Kth_Largest_Element_in_an_Array").  Partition the array
# with numbers larger than median at swapped to the left, numbers higher swapped to the right and numbers same
# unswapped.  Remap indices such that odd are filled first, then wrap around to start again with even.
# Time - O(n log n)
# Space - O(1)

class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        median = nums[len(nums)//2]

        # map larger to last even, smaller to first odd
        def mapping(i):
            return (i*2 + 1) % (len(nums) | 1)      # modulo next odd number

        # < left are > median, >= left and < i are == median, > right are < median
        # >= i and <= right are unsorted
        left, i, right = 0, 0, len(nums) - 1

        while i <= right:
            if nums[mapping(i)] > median:
                nums[mapping(i)], nums[mapping(left)] = nums[mapping(left)], nums[mapping(i)]
                left += 1
                i += 1
            elif nums[mapping(i)] < median:
                nums[mapping(i)], nums[mapping(right)] = nums[mapping(right)], nums[mapping(i)]
                right -= 1
            else:
                i += 1