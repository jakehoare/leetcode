_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/ransom-note/
# Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function
# that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.
# Each letter in the magazine string can only be used once in your ransom note.
# You may assume that both strings contain only lowercase letters.

# Count all chars in ransom note asd magazines. If any char is in ransom note but not magazine or has a lower count in
# magazine then return False.
# Time - O(m + n)
# Space - O(1)

from collections import Counter

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        mag_count = Counter(magazine)
        ransom_count = Counter(ransomNote)

        for c in ransom_count:
            if c not in mag_count or mag_count[c] < ransom_count[c]:
                return False

        return True