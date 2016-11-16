_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/word-break-ii/
# Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.
# Return all such possible sentences.

# Test if word can be broken as per problem 139.  For all prefixes of s in the dictionary, recurse on the suffix.
# Time - O(n**3 * 2**(n-1))
# Space - O(n * 2**(n-1)), 2**(n-1) possible partitions of string of length n (every combination of gaps between words)
# each partiton is of length n.  Memo for shorter suffixes does not impact big O.

class Solution(object):

    def canBreak(self, s, wordDict):
        can_make = [False] * (len(s)+1)         # can_make[i] is True if can make prefix of length i
        can_make[0] = True
        for i in range(1, len(s)+1):            # prefix length
            for j in range(i-1, -1, -1):        # j is existing prefix, start with longest + shortest new word
                if can_make[j] and s[j:i] in wordDict:
                    can_make[i] = True
                    break
        return can_make[-1]


    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        if not self.canBreak(s, wordDict):
            return []
        result_lists = self.break_word(s, 0, wordDict, {})
        return [" ".join(result) for result in result_lists]    # convert back to strings


    def break_word(self, s, left, wordDict, memo):      # break from s[left] onwards

        if left >= len(s):      # base case
            return [[]]
        if left in memo:
            return memo[left]

        results = []
        for i in range(left+1, len(s)+1):       # try all possible prefixes
            prefix = s[left:i]
            suffix_breaks = self.break_word(s, i, wordDict, memo)
            if suffix_breaks and prefix in wordDict:
                for suffix_break in suffix_breaks:
                    results.append([prefix] + suffix_break)

        memo[left] = results[:]
        return results
