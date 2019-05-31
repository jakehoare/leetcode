_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/find-and-replace-in-string/
# To some string S, we will perform some replacement operations that replace groups of letters with new ones
# (not necessarily the same size).
# Each replacement operation has 3 parameters: a starting index i, a source word x and a target word y.
# The rule is that if x starts at position i in the original string S, then we will replace that occurrence of x with y.
# If not, we do nothing.
# For example, if we have S = "abcd" and we have some replacement operation i = 2, x = "cd", y = "ffff", then
# because "cd" starts at position 2 in the original string S, we will replace it with "ffff".
# Using another example on S = "abcd", if we have both the replacement operation i = 0, x = "ab", y = "eee",
# as well as another replacement operation i = 2, x = "ec", y = "ffff", this second operation does nothing because in
# the original string S[2] = 'c', which doesn't match x[0] = 'e'.
# All these operations occur simultaneously.  It's guaranteed that there won't be any overlap in replacement:
# for example, S = "abc", indexes = [0, 1], sources = ["ab","bc"] is not a valid test case.

# Convert to mutable list of chars. For each index, if substring string of length source is same as source string,
# replace the first char with the target and remaining chars of source with empty strings.
# Time - O(min(k, nm)) for n replacements of max length m, len(S) == k
# Space - O(k + mn)

class Solution(object):
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        replaced = [c for c in S]               # convert to list

        for i, src, tgt in zip(indexes, sources, targets):

            n = len(src)
            if S[i:i + n] == src:
                replaced[i] = tgt
                replaced[i + 1:i + n] = [""] * (n - 1)

        return "".join(replaced)