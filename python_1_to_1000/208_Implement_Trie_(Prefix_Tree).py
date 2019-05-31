_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/implement-trie-prefix-tree/
# Implement a trie with insert, search, and startsWith methods.
# You may assume that all inputs are consist of lowercase letters a-z

# Node stores dictionary mapping letters to child nodes.  Array would use fixed space regardless of actual nb children.
# Note that node does not explicitly store letter.
# Time - O(n) to create where n is total length of all words, O(k) to search where k is length of word.
# Space - O(n)

class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = {}      # mapping from letter to child TrieNodes
        self.terminal = False   # flag indicates whole word

class Trie(object):

    def __init__(self):
        self.root = TrieNode()
        self.root.terminal = True   # empty string is a whole word

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for c in word:
            if c not in node.children:  # create a node if it does not exist
                node.children[c] = TrieNode()
            node = node.children[c]
        node.terminal = True            # set to True at end of word

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for c in word:
            if c in node.children:
                node = node.children[c]
            else:
                return False
        return node.terminal            # only True if terminal

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for c in prefix:
            if c in node.children:
                node = node.children[c]
            else:
                return False
        return True