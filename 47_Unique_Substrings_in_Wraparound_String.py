_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/unique-substrings-in-wraparound-string/
# Consider the string s to be the infinite wraparound string of "abcdefghijklmnopqrstuvwxyz", so s will look like
# this: "...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....".
# Now we have another string p. Your job is to find out how many unique non-empty substrings of p are present in s.
# In particular, your input is the string p and you need to output the number of different non-empty substrings of p
# in the string s. p consists of only lowercase English letters.

# Record the longest substring ending with each of the 26 letters. Iterate over p, incrementing the substring length
# if letter incerements previous. Update max substring ending with current letter. Result is sum of all substrings for
# all letters.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        substring_ending = [0] * 26  # length of longest substring ending with char
        length = 0

        for i, c in enumerate(p):

            if i != 0 and (ord(c) == ord(p[i - 1]) + 1 or ord(c) == ord(p[i - 1]) - 25):
                length += 1
            else:
                length = 1

            substring_ending[ord(c) - ord("a")] = max(substring_ending[ord(c) - ord("a")], length)

        return sum(substring_ending)
