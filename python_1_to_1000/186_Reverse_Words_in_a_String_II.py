_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/reverse-words-in-a-string-ii/
# Given an input string, reverse the string word by word. A word is defined as a sequence of non-space characters.
# The input string does not contain leading or trailing spaces and the words are always separated by a single space.

# Revese entire string then reverse each word individually.
# Alternatively use built-in reverse() and reversed() functions.
# Time - O(n)
# Space - O(1)

class Solution:
    # @param s, a list of 1 length strings, e.g., s = ['h','e','l','l','o']
    # @return nothing
    def reverseWords(self, s):

        self.reverse(s, 0, len(s)-1)

        s.append(' ')   # temporary space to signify end of last word
        start = 0
        for i in range(len(s)):
            if s[i] == ' ':
                self.reverse(s, start, i-1)     # reverse word from start to i-1
                start = i+1                     # start of next word
        s.pop()

    def reverse(self, s, left, right):
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


class Solution2:
    def reverseWords(self, s):
        s.reverse()
        s.append(' ')
        start = 0
        for i in range(len(s)):
            if s[i] == ' ':
                s[start:i] = reversed(s[start:i])
                start = i+1
        s.pop()