_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/count-binary-substrings/
# Give a string s, count the number of non-empty (contiguous) substrings that have the same number of 0's and 1's,
# and all the 0's and all the 1's in these substrings are grouped consecutively.
# Substrings that occur multiple times are counted the number of times they occur.

# When a sequence of one digit ends, count the required substrings using this sequence and the previous sequence
# (which uses the other digit). Count as many substrings as the lower of the sequence length and previous sequence
# length.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        seq, prev_seq = 1, 0                    # lengths of the current and previous sequences
        count = 0

        for i, c in enumerate(s[1:], 1):        # first digit already used

            if c != s[i - 1]:                   # c is different from previous char
                count += min(seq, prev_seq)     # add all balanced substrings
                seq, prev_seq = 1, seq
            else:
                seq += 1

        return count + min(seq, prev_seq)       # add final balanced substrings