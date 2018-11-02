_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/reverse-only-letters/
# Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place,
# and all letters reverse their positions.

# Convert to list. 2 pointers start from left and right. Move each pointer inwards until they both reach letters.
# Swap the letters and move the pointers another step each. Stop when pointers overlap.
# Time - O(n)
# Space - O(n)

import string

class Solution:
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        letters = set(string.ascii_lowercase + string.ascii_uppercase)

        S = [c for c in S]
        left, right = 0, len(S) - 1

        while left < right:

            while left < right and S[left] not in letters:
                left += 1
            while left < right and S[right] not in letters:
                right -= 1

            S[left], S[right] = S[right], S[left]
            left += 1
            right -= 1

        return "".join(S)