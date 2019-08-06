_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/remove-vowels-from-a-string/
# Given a string S, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.

# Create a set of vowels and return the join of all chars of S that are not in the set.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def removeVowels(self, S):
        """
        :type S: str
        :rtype: str
        """
        vowels = set("aeiou")
        return "".join(c for c in S if c not in vowels)
