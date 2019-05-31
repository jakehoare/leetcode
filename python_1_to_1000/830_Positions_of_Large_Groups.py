_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/positions-of-large-groups/
# In a string S of lowercase letters, these letters form consecutive groups of the same character.
# For example, a string like S = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z" and "yy".
# Call a group large if it has 3 or more characters. Find the starting and ending positions of every large group.
# The final answer should be in lexicographic order.

# Iterate over S. When the next char is different from the previous char, add to the result if the group length >= 3.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        result = []
        start = 0

        for i, c in enumerate(S):

            if i == len(S) - 1 or c != S[i + 1]:
                if i - start >= 2:
                    result.append([start, i])
                start = i + 1                       # update start index of next group

        return result