_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/letter-case-permutation/
# Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.
# Return a list of all possible strings we could create.

# Start with empty list as the only result. For each char in S, if char is a digit append it ot each existing result.
# Else append the upper and lower case of char to each existing result.
# Time - O(n * 2**n), since 2**n possible results of length n
# Space - O(n * 2**n)

class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        permutations = [[]]

        for c in S:

            if "0" <= c <= "9":
                for perm in permutations:
                    perm.append(c)

            else:

                new_permutations = []
                upper, lower = c.upper(), c.lower()

                for perm in permutations:
                    new_permutations.append(perm + [upper])
                    perm.append(lower)
                    new_permutations.append(perm)

                permutations = new_permutations

        return ["".join(perm) for perm in permutations]     # convert lists of chars to strings