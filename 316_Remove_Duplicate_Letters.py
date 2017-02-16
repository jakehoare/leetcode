_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/remove-duplicate-letters/
# Given a string which contains only lowercase letters, remove duplicate letters so that every letter appear once
# and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

# Find the first instance of the lexicographically first letter in the string.  If the suffix starting from this letter
# contains all of the letters in the string, then add this to the result and recurse on the remainder of the string
# having removed all of this letter.  If the suffix does not contain all letters, try the lexicographically next letter.
# A letter is added to the result when the prefix does not contain all instances of any other letter.
# Time - O(n * k) where k is the size of the alphabet
# Space - O(n)

class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_set = sorted(set(s))
        for c in s_set:
            suffix = s[s.index(c):]
            if len(set(suffix)) == len(s_set):
                return c + self.removeDuplicateLetters(suffix.replace(c, ""))
        return ""
