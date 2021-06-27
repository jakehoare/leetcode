_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/count-of-smaller-numbers-after-self/
# You are given an integer array nums and you have to return a new counts array. The counts array has the property
# where counts[i] is the number of smaller elements to the right of nums[i].

# Merge sort, counting the smaller elements to the right during merging.
# Helper function sorts the original indices of the input.
# Merge in decreasing order, incrementing smallest when all right array are smaller than largest of left array.
# Time - O(n log n)
# Space - O(n)

class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def helper(indices):
            mid = len(indices) / 2
            if mid == 0:
                return indices
            
            left, right = helper(indices[:mid]), helper(indices[mid:])
            
            for i in range(len(indices))[::-1]: # Rebuild indices from largest to smallest num.
                if not right or left and nums[left[-1]] > nums[right[-1]]:
                    indices[i] = left.pop()
                    smaller[indices[i]] += len(right) # All right are smaller than largest left.
                else:
                    indices[i] = right.pop()
            
            return indices
        
        
        smaller = [0 for _ in range(len(nums))]
        helper([i for i in range(len(smaller))])
        return smaller
