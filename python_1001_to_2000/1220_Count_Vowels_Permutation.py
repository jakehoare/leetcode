_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/count-vowels-permutation/
# Given an integer n, your task is to count how many strings of length n can be formed under the following rules:
# Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
# Each vowel 'a' may only be followed by an 'e'.
# Each vowel 'e' may only be followed by an 'a' or an 'i'.
# Each vowel 'i' may not be followed by another 'i'.
# Each vowel 'o' may only be followed by an 'i' or a 'u'.
# Each vowel 'u' may only be followed by an 'a'.
# Since the answer may be too large, return it modulo 10^9 + 7.

# Create a mapping from each vowel to the number of permutations ending with that vowel.
# For each new letter, update the permutations from all previous vowels that can be followed by the new vowel.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def countVowelPermutation(self, n):
        """
        :type n: int
        :rtype: int
        """
        counts = {vowel: 1 for vowel in "aeiou"}    # 1 permutation for each letter

        for _ in range(n - 1):
            new_counts = {}
            new_counts["a"] = counts["e"] + counts["i"] + counts["u"]
            new_counts["e"] = counts["a"] + counts["i"]
            new_counts["i"] = counts["e"] + counts["o"]
            new_counts["o"] = counts["i"]
            new_counts["u"] = counts["i"] + counts["o"]
            counts = new_counts

        return sum(counts.values()) % (10 ** 9 + 7)
