_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/unique-letter-string/
# A character is unique in string S if it occurs exactly once in it.
# For example, in string S = "LETTER", the only unique characters are "L" and "R".
# Let's define UNIQ(S) as the number of unique characters in string S.
# For example, UNIQ("LETTER") =  2.
# Given a string S with only uppercases, calculate the sum of UNIQ(substring) over all non-empty substrings of S.
# If there are two or more equal substrings at different positions in S, we consider them different.
# Since the answer can be very large, return the answer modulo 10 ^ 9 + 7.

# For each letter, make a list of indices in S of the letter. For each in index in each list part from the first and
# last, we can make subarrays where the letter is unique with left edges up to the previous index and right edges up
# to the next index.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def uniqueLetterString(self, S):
        """
        :type S: str
        :rtype: int
        """
        unique = 0
        indices = [[-1] for _ in range(26)]

        for i, c in enumerate(S):
            indices[ord(c) - ord("A")].append(i)

        for index_list in indices:

            index_list.append(len(S))
            for i in range(1, len(index_list) - 1):
                unique += (index_list[i] - index_list[i - 1]) * (index_list[i + 1] - index_list[i])

        return unique % (10 ** 9 + 7)