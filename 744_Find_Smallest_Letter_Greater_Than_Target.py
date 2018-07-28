_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/find-smallest-letter-greater-than-target/
# Given a list of sorted characters letters containing only lowercase letters, and given a target letter target,
# find the smallest element in the list that is larger than the given target.
# Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.

# Binary search for the next greater letter.
# Time - O(log n)
# Space - O(1)

class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        left, right = 0, len(letters)   # initial search space is first letter to beyond last letter (inclusive)

        while left < right:             # stop if left == right

            mid = (left + right) // 2

            if target >= letters[mid]:  # search RHS excluding mid
                left = mid + 1
            else:                       # mid could be next greater letter
                right = mid

        letters.append(letters[0])      # handle wrap around
        return letters[left]