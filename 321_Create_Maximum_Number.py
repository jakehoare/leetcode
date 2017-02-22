_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/create-maximum-number/
# Given two arrays of length m and n with digits 0-9 representing two numbers. Create the maximum number of
# length k <= m + n from digits of the two. The relative order of the digits from the same array must be preserved.
# Return an array of the k digits.

# For each partition of i digits from nums1 and (i from 0 to k) and k-i digits from nums 2, find the max number from
# each nums list using that many digits.  The overall max is the merge of 2 individual max numbers.  Merge by taking
# the larger digit from the front, if equal look forward to the next position where the digits are different and take
# the larger.  Single num largest uses a stack, popping all smaller digits provided there are enough remaining and
# and adding whenever the stack has capacity.
# Time - O(k * n**3), k*n to check each partition and convert to int, n**2 to merge (n to max_single() irrelevant)
# Space - O(n)

class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        max_number = 0
        for i in range(k + 1):
            if i <= len(nums1) and k - i <= len(nums2):
                max1 = self.max_single(nums1, i)
                max2 = self.max_single(nums2, k - i)
                merged = self.merge(max1, max2)
                max_number = max(max_number, int("".join(map(str, merged))))
        return [int(c) for c in str(max_number)]


    def max_single(self, nums, k):
        stack, n = [], len(nums)
        for i, num in enumerate(nums):
            # stack not empty and num is more than top of stack and stack + remaining nums are more than k
            while stack and num > stack[-1] and (len(stack) + (n - i) > k):
                stack.pop()
            if len(stack) < k:
                stack.append(num)
        return stack


    def merge(self, nums1, nums2):
        i, j = 0, 0
        merged = []

        while i < len(nums1) and j < len(nums2):

            if nums1[i] < nums2[j]:
                use1 = False
            elif nums1[i] > nums2[j]:
                use1 = True
            else:       # nums1[i] == nums2[j]
                shift = 1
                while i+shift < len(nums1) and j+shift < len(nums2) and nums1[i+shift] == nums2[j+shift]:
                    shift += 1
                if i+shift == len(nums1):
                    use1 = False
                elif j+shift == len(nums2):
                    use1 = True
                elif nums2[j+shift] > nums1[i+shift]:
                    use1 = False
                else:
                    use1 = True

            if use1:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1

        return merged + nums1[i:] + nums2[j:]

