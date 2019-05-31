_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/word-search-ii/
# Given a 2D board and a list of words from the dictionary, find all words in the board.
# Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those
# horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

# Build a trie of the words to be found. For each starting cell of the board, if cell contains same letter as a child
# of the trie node then update node to child and recurse on 4 surrounding cells.  Add complete words to found list.
# Overwrite letters used in each dfs with '*' char (not used in words) during recursion then replace before return.
# Time - O(m * n * t) where board is m by n and t is total number of chars in all words
# Space - O(t) for trie

class Node:
    def __init__(self):
        self.children = {}  # map letter to child node
        self.word = None

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        root = Node()
        for word in words:      # build a trie
            node = root
            for c in word:
                if c not in node.children:
                    node.children[c] = Node()
                node = node.children[c]
            node.word = word    # node is end of complete word

        found = []
        for r in range(len(board)):
            for c in range(len(board[0])):
                self.search(board, root, r, c, found)
        return found

    def search(self, board, node, r, c, found):     # depth first search of board

        if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
            return

        letter = board[r][c]
        if letter not in node.children:
            return

        node = node.children[letter]
        if node.word:
            found.append(node.word)
            node.word = None    # avoid duplication of results

        board[r][c] = '*'       # temporarily flag this cell as being used
        self.search(board, node, r+1, c, found)
        self.search(board, node, r-1, c, found)
        self.search(board, node, r, c+1, found)
        self.search(board, node, r, c-1, found)
        board[r][c] = letter    # replace cell contents
