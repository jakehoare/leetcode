_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/valid-word-abbreviation/
# Given a non-empty string s and an abbreviation abbr, return whether the string matches with the given abbreviation.
# Assume s contains only lowercase letters and abbr contains only lowercase letters and digits.

# Iterate over abbreviation. If char then check if matches words and increment both pointer. If digit, parse the
# number and move forward the pointer in word. Return false if pointers do not reach the end of word and abbr
# simultaneously.
# Time - O(n) length of abbr
# Space - O(1)

class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        i, j = 0, 0

        while j < len(abbr):

            if abbr[j] < "a":               # digit

                if abbr[j] == "0":          # cannot lead with zero or skip zero letters
                    return False
                count = 0
                while j < len(abbr) and abbr[j] < "a":
                    count = count * 10 + int(abbr[j])
                    j += 1
                i += count

            else:                           # letter
                if i >= len(word) or abbr[j] != word[i]:
                    return False
                i += 1
                j += 1

        return i == len(word)               # must use all of word

