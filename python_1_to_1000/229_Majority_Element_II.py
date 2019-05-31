_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/majority-element-ii/
# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
# The algorithm should run in linear time and in O(1) space.

# There can be at most 2 elements that make up more than 1/3 of the input.  Maintain 2 candidates, incrementing their
# counts as we find new instances.  If an element is neither candidate then decrement count of both candidates.
# If an element is more than 1/3 of an array then it will remain so when 3 different elements are removed.
# If a count reduces to zero then the next element is a new candidate.
# Finally check if candidates are actually > 1/3 of array.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        cand1, count1 = None, 0
        cand2, count2 = None, 0

        for num in nums:
            if num == cand1:    # increment count of candidate
                count1 += 1
            elif num == cand2:  # increment count of candidate
                count2 += 1
            elif count1 == 0:   # new cancidate
                cand1 = num
                count1 = 1
            elif count2 == 0:   # new cancidate
                cand2 = num
                count2 = 1
            else:       # 'remove' 3 different elements (cand1, cand2, num) from count
                count1 -= 1
                count2 -= 1

        # check if candidates are more than 1/3 of list length
        return [n for n in (cand1, cand2) if nums.count(n) > len(nums) // 3]

