_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/alien-dictionary/
# There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you.
# You receive a list of words from the dictionary, where words are sorted lexicographically by the rules of this
# new language. Derive the order of letters in this language.

# For each character, count the number of chars that appear before it and create a set of chars that appear after it.
# The first difference in chars at the same position for consecutive words in the dictionary gives an ordered pair
# of chars.  Find a topologial ordering of the resulting directed graph by repeatedly removing chars that have no
# earlier chars remaining.
# Time - O(n), total number of chars in all words
# Space - O(m**2), nb chars in alphabet - order can be set of all chars for each char

from collections import defaultdict

class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        after = defaultdict(int)    # key is char, value is nb times char depends on a previous char
        order = defaultdict(set)    # key is char, value is set of chars appearing after char
        seen = set(words[0])        # all chars found so far

        for i in range(1, len(words)):
            diff_to_prev = False

            for j, c in enumerate(words[i]):
                seen.add(c)         # add every char of every word to seen

                # new difference from previous word at this position
                if j < len(words[i-1]) and not diff_to_prev and c != words[i-1][j]:
                    if c not in order[words[i-1][j]]:   # have not seen this ordering before
                        order[words[i-1][j]].add(c)
                        after[c] += 1
                    diff_to_prev = True

            if not diff_to_prev and len(words[i-1]) > len(words[i]):    # no differences and longer word first
                return ""

        for c in seen:              # all chars depend on at least zero previous chars
            if c not in after:
                after[c] = 0

        frontier = set()            # frontier have no dependencies
        for a in after:
            if after[a] == 0:
                frontier.add(a)

        letters = []
        while frontier:
            b = frontier.pop()      # add char from frontier to result
            del after[b]
            letters.append(b)
            for a in order[b]:      # decrement dependency count of those appearing after b
                after[a] -= 1
                if after[a] == 0:
                    frontier.add(a)

        if after:
            return ""

        return "".join(letters)

