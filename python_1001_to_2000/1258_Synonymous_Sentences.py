_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/synonymous-sentences/
# Given a list of pairs of equivalent words synonyms and a sentence text,
# return all possible synonymous sentences sorted lexicographically.

# Group synonyms together with union-find.
# Each synonym is mapped to a parent. The ultimate parent is a group exemplar.
# For each pair of synonymous words, find their parents and join their parent's groups.
# Then map each ultimate parent to all synonyms.
# For each word in the text, extend each previous result with each synonym.
# Alternatively, breadth-first search the graph of synonyms.
# Time - O(s log* m + n**2 * k**n) where s log* m is for s synonym pairs and m synonym words and
# n**2 * k**n is for n words in text each with k synonyms.
# Space - O(s + n * k**n)

from collections import defaultdict

class Solution(object):
    def generateSentences(self, synonyms, text):
        """
        :type synonyms: List[List[str]]
        :type text: str
        :rtype: List[str]
        """
        parents = {}                # map node to parent (map to self if no parent)

        def find(s):                # find ultimate parent (could also collapse)
            if s not in parents:
                parents[s] = s
            while parents[s] != s:
                s = parents[s]
            return s

        for a, b in synonyms:       # join groups of ultimate parents
            parents[find(a)] = find(b)

        parent_to_synonyms = defaultdict(list)  # map each parent to all synonyms
        for word in parents:
            parent_to_synonyms[find(word)].append(word)

        results = [[""]]

        for word in text.split():
            new_results = []
            synonyms = parent_to_synonyms.get(find(word), [word])   # default to word of no synonyms
            for synonym in synonyms:
                for result in results:
                    new_results.append(result[:] + [synonym])
            results = new_results

        return [" ".join(result[1:]) for result in sorted(results)] # sort lexicographically
