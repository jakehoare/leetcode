_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/similar-string-groups/
# Two strings X and Y are similar if we can swap two letters (in different positions) of X, so that it equals Y.
# For example, "tars" and "rats" are similar (swapping at positions 0 and 2), and "rats" and "arts" are similar,
# but "star" is not similar to "tars", "rats", or "arts".
# Together, these form two connected groups by similarity: {"tars", "rats", "arts"} and {"star"}.
# Notice that "tars" and "arts" are in the same group even though they are not similar.
# Formally, each group is such that a word is in the group if and only if it is similar to at least one other
# word in the group.
# We are given a list A of strings. Every string in A is an anagram of every other string in A. Count the groups.

# For each word, depth-first search all similar words to visit all words in a group. 2 different approaches are taken
# to find similar words depensing whether there are few long words or many short words.
# If few long words, create a mapping from each word to the set of its similar words. Mapping is made by iterating over
# all pairs of words and checking if similar.
# If many short words, find similar words by swapping all pairs of characters in a word.
# Time - O(min(W N**2, N W**3)
# Space - O(N W**3) since each word may have W**2 neighbours

from collections import defaultdict

class Solution(object):
    def numSimilarGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        N, W = len(A), len(A[0])
        word_swap = defaultdict(set)

        if N < 2 * W:           # if few long words

            for i, w1 in enumerate(A):
                for j in range(i + 1, len(A)):
                    w2 = A[j]
                    if len([True for c1, c2 in zip(w1, w2) if ord(c1) - ord(c2) != 0]) == 2:
                        word_swap[w1].add(w2)
                        word_swap[w2].add(w1)
        else:
            A_set = set(A)

        def get_neighbours(a):
            if word_swap:
                return word_swap[a]
            neighbours = set()
            for i in range(W - 1):
                for j in range(i + 1, W):
                    if a[i] != a[j]:
                        neighbour = a[:i] + a[j] + a[i + 1:j] + a[i] + a[j + 1:]
                        if neighbour in A_set:
                            neighbours.add(neighbour)

            return neighbours

        groups = 0
        visited = set()

        def dfs(w):
            visited.add(w)
            for nbor in get_neighbours(w):
                if nbor not in visited:
                    dfs(nbor)

        for word in A:
            if word in visited:
                continue
            groups += 1
            dfs(word)

        return groups

