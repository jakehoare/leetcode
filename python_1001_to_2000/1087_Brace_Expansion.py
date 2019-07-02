_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/brace-expansion/
# A string S represents a list of words.
# Each letter in the word has 1 or more options.
# If there is one option, the letter is represented as is.
# If there is more than one option, then curly braces delimit the options.
# For example, "{a,b,c}" represents options ["a", "b", "c"].
# For example, "{a,b,c}d{e,f}" represents the list ["ade", "adf", "bde", "bdf", "cde", "cdf"].
# Return all words that can be formed in this manner, in lexicographical order.

# Create a list of lists where each inner list is a sorted group of words.
# Then depth-first search. For each group, add all words to the current partial result and recurse to the next group.
# Time - O(g**2 * n**g) - as space complexity below except each result is built by adding individual chars.
# Space - O(g * n**g) for g groups of length n since each result is of length g and there are n possibilities for
# each char.

class Solution(object):
    def expand(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        group_start = 0
        groups = []

        while group_start < len(S):
            while S[group_start] in "}{":     # ignore previous closing or current opening braces
                group_start += 1
            group_end = group_start
            while group_end < len(S) and S[group_end] not in "{}":      # find end of current group
                group_end += 1
            groups.append(sorted(S[group_start:group_end].split(",")))  # sort words in group
            group_start = group_end + 1

        results = []
        def expand(group, partial):
            if group == len(groups):
                results.append(partial)
                return
            for c in groups[group]:
                expand(group + 1, partial + c)

        expand(0, "")
        return results
