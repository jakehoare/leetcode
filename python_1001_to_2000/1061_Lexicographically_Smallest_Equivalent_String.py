_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/lexicographically-smallest-equivalent-string/
# Given strings A and B of the same length, we say A[i] and B[i] are equivalent characters.
# For example, if A = "abc" and B = "cde", then we have 'a' == 'c', 'b' == 'd', 'c' == 'e'.
# Equivalent characters follow the usual rules of any equivalence relation:
# Reflexivity: 'a' == 'a'
# Symmetry: 'a' == 'b' implies 'b' == 'a'
# Transitivity: 'a' == 'b' and 'b' == 'c' implies 'a' == 'c'
# For example, given the equivalency information from A and B above, S = "eed", "acd", and "aab" are equivalent strings,
# and "aab" is the lexicographically smallest equivalent string of S.
# Return the lexicographically smallest equivalent string of S by using the equivalency information from A and B.

# Create a mapping from each char to its direct equivalents.
# For each char of S, explore the map of all equivalents and set the minimum equivalent of all chars visited.
# Memoize the minimum equivalents.
# Time - O(n)
# Space - O(n)

from collections import defaultdict

class Solution(object):
    def smallestEquivalentString(self, A, B, S):
        """
        :type A: str
        :type B: str
        :type S: str
        :rtype: str
        """
        equivalents = defaultdict(set)  # map char to its directly connected equivalents
        for a, b in zip(A, B):
            equivalents[a].add(b)
            equivalents[b].add(a)

        minimum = {}                    # map char to its minimum equivalent

        def get_minimum(char):          # return the minimum equivalent
            if char in minimum:
                return minimum[char]

            result = char
            visited = set()
            queue = {char}

            while queue:
                c = queue.pop()
                if c in visited:
                    continue
                visited.add(c)
                result = min(result, c)
                queue |= equivalents[c] # add all equivalents to the queue

            for v in visited:       # minimum equivalent for all visited is set to result
                minimum[v] = result
            return result

        return "".join(get_minimum(c) for c in S)
