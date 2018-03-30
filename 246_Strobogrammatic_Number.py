_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/strobogrammatic-number/
# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
# Write a function to determine if a number is strobogrammatic. The number is represented as a string.
# For example, the numbers "69", "88", and "818" are all strobogrammatic.

# Iterate over nums, matching digits at the front with rotated digits at the back.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        strob = {'0':'0', '1':'1', '8':'8', '6':'9', '9':'6'}       # map digit to its rotation

        for left in range((len(num) + 1) // 2):                     # include middle digit if odd length

            right = len(num) - 1 - left
            if num[left] not in strob or strob[num[left]] != num[right]:
                return False

        return True