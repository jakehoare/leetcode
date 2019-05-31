_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/palindrome-permutation-ii/
# Given a string s, return all the palindromic permutations (without duplicates) of it.
# Return an empty list if no palindromic permutation could be formed.

# Firstly find the only char with an odd count, if there is any.  If more than 1 odd count char then return [].
# Remove one instance of this from the count so all chars now have even counts.
# Build all possible permutations of the remaining chars recursively by adding one instance of any char with a
# non-zero count to partial list and decrementing the count of this char by 2.  Track the number of remaining
# chars to add such that when this is zero we have a resulting half-palindrome.  Finally build full palindromes from
# half and odd_char.
# Time - O(n * n!), n! permutations of length n
# Space - O(n * n!)

from collections import Counter

class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        char_counts = Counter(s)
        odd_char = ""                   # char with an odd count

        for char, count in char_counts.items():
            if count % 2 != 0:
                if odd_char:
                    return []               # more than one odd count, cannot form palindromes
                odd_char = char
                char_counts[odd_char] -= 1  # decrement counter

        palindromes = []
        self.build_palindromes(palindromes, [], char_counts, len(s)//2)
        return ["".join(p + [odd_char] + p[::-1]) for p in palindromes]


    def build_palindromes(self, palindromes, partial, char_counts, remaining):

        if remaining == 0:
            palindromes.append(partial[:])      # copy of partial

        for c in char_counts.keys():
            if char_counts[c] == 0:             # skip if count is zero
                continue

            char_counts[c] -= 2                 # decrement count and add c to partial list
            partial.append(c)
            self.build_palindromes(palindromes, partial, char_counts, remaining-1)
            partial.pop()                      # revert count and partial list
            char_counts[c] += 2

