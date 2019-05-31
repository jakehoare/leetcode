_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/shifting-letters/
# We have a string S of lowercase letters, and an integer array shifts.
# Call the shift of a letter, the next letter in the alphabet, (wrapping around so that 'z' becomes 'a').
# For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.
# Now for each shifts[i] = x, we want to shift the first i+1 letters of S, x times.
# Return the final string after all such shifts to S are applied.

# Iterate backwards over shifts. Maintain the cumulative_shift, adding each shift and shifting the char by the
# cumulative_shift.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        s = [ord(c) - ord("a") for c in S]              # convert to list of integers in [0, 25]

        cumulative_shift = 0
        for i in range(len(s) - 1, -1, -1):
            cumulative_shift += shifts[i]
            s[i] = (s[i] + cumulative_shift) % 26       # apply cumulative_shift to char

        return "".join(chr(c + ord("a")) for c in s)