_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/reverse-vowels-of-a-string/
# Write a function that takes a string as input and reverse only the vowels of a string.

# Find list of indices of vowels in s. Swap vowel at first index with vowel at last index, until meeting in middle
# of list of vowels.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = {"a", "e", "i", "o", "u"}
        vowels |= {c.upper() for c in vowels}

        vowel_i = [i for i, c in enumerate(s) if c in vowels]
        n_vowel = len(vowel_i)

        s = [c for c in s]
        for j in range(n_vowel // 2):
            s[vowel_i[j]], s[vowel_i[n_vowel - j - 1]] = s[vowel_i[n_vowel - j - 1]], s[vowel_i[j]]

        return "".join(s)