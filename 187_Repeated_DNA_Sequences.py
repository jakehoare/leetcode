_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/repeated-dna-sequences/
# All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG".
# When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.
# Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

# Store all substrings of length 10 in a set, if substring is duplicated add to result set.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        substrings, repeated = set(), set()
        TARGET = 10

        for i in range(len(s)-TARGET+1):

            substring = s[i:i+TARGET]
            if substring in substrings:
                repeated.add(substring)
            else:
                substrings.add(substring)

        return list(repeated)       # convert set to list