_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/sentence-similarity-ii/
# Given two sentences words1, words2 (each represented as an array of strings), and a list of similar word pairs pairs,
# determine if two sentences are similar.
# For example, words1 = ["great", "acting", "skills"] and words2 = ["fine", "drama", "talent"] are similar, if the
# similar word pairs are pairs = [["great", "good"], ["fine", "good"], ["acting","drama"], ["skills","talent"]].
# Note that the similarity relation is transitive. For example, if "great" and "good" are similar, and "fine" and
# "good" are similar, then "great" and "fine" are similar.
# Similarity is also symmetric. For example, "great" and "fine" being similar is the same as "fine" and "great"
# being similar.
# Also, a word is always similar with itself. For example, the sentences words1 = ["great"], words2 = ["great"],
# pairs = [] are similar, even though there are no specified similar word pairs.
# Finally, sentences can only be similar if they have the same number of words. So a sentence like words1 = ["great"]
# can never be similar to words2 = ["doubleplus","good"].

# Union-find. Create tree linking each word to its parent. Find parents of new words by moving up tree, collapsing
# links from parent to grandparent. If either word is not in tree then make its parent the parent of the other word.
# Time - O((n + p) log p ), len(words1) = n and len(pairs) = w2. p log p to create mapping + n log p to check.
# Space - O(n)

class Solution(object):
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        def find(word):
            if word not in mapping:
                return None
            while mapping[word] != word:
                mapping[word] = mapping[mapping[word]]      # collapse link from parent to grandparent
                word = mapping[word]                        # move up
            return word

        if len(words1) != len(words2):                      # early return
            return False
        mapping = {}                                        # map word to its parent, which maybe itself

        for w1, w2 in pairs:
            p1, p2 = find(w1), find(w2)
            if p1:
                if p2:
                    mapping[p1] = p2                        # may already be equal
                else:
                    mapping[w2] = p1                        # insert mapping for w1
            else:
                if p2:
                    mapping[w1] = p2                        # insert mapping for w2
                else:
                    mapping[w1] = mapping[w2] = w1          # new pair separated from other mappings

        for w1, w2 in zip(words1, words2):

            if w1 == w2:
                continue

            p1, p2 = find(w1), find(w2)
            if not p1 or not p2 or p1 != p2:                # no or different parents
                return False

        return True
