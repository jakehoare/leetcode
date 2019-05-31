_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/prefix-and-suffix-search/
# Given many words, words[i] has weight i.
# Design a class WordFilter that supports one function, WordFilter.f(String prefix, String suffix).
# It will return the word with given prefix and suffix with maximum weight. If no word exists, return -1.

# Create a trie to store each word in its usual order (forwards) and a trie to store each word backwards.
# Find the sets of all words that match prexis and suffix from their respective tries. Take the max weight from the
# set intersection.
# Time - O(n) to __init__ where n is the total umber of chars in all words. O(p + s + k) where p = len(prefix),
# s = len(suffix), k = number of words.
# Space - O(n)

class WordFilter(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.prefix_root = [set(), [None for _ in range(26)]]   # trie node is set of words and list of next nodes
        self.suffix_root = [set(), [None for _ in range(26)]]   # for each char
        self.weights = {}                                       # map word to weight

        def insert(word, forwards):                             # insert a word into a trie
            if forwards:
                node = self.prefix_root
                iterate_word = word
            else:
                node = self.suffix_root
                iterate_word = word[::-1]

            node[0].add(word)
            for c in iterate_word:
                if not node[1][ord(c) - ord("a")]:              # create a new node of None
                    node[1][ord(c) - ord("a")] = [set(), [None for _ in range(26)]]
                node = node[1][ord(c) - ord("a")]
                node[0].add(word)

        for weight, word in enumerate(words):
            self.weights[word] = weight
            insert(word, True)
            insert(word, False)

    def f(self, prefix, suffix):
        """
        :type prefix: str
        :type suffix: str
        :rtype: int
        """

        def find_words(word, forwards):
            if forwards:
                node = self.prefix_root
                iterate_word = word
            else:
                node = self.suffix_root
                iterate_word = word[::-1]

            for c in iterate_word:
                node = node[1][ord(c) - ord("a")]
                if not node:
                    return -1       # early return if cannot match whole prefix or suffix
            return node[0]

        prefix_matches = find_words(prefix, True)
        suffix_matches = find_words(suffix, False)
        if prefix_matches == -1 or suffix_matches == -1:
            return -1

        matches = prefix_matches & suffix_matches
        weight = -1
        for match in matches:
            weight = max(weight, self.weights[match])
        return weight