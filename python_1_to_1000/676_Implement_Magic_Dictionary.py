_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/implement-magic-dictionary/
# Implement a magic directory with buildDict, and search methods.
# For the method buildDict, you'll be given a list of non-repetitive words to build a dictionary.
# For the method search, you'll be given a word, and judge whether if you modify exactly one character into another
# character in this word, the modified word is in the dictionary you just built.

# Create a trie where each node is a mapping from a letter to the next node (which is itself a mapping). Terminal
# nodes at the end of words are signified by a mapping to '#'. Search works by depth first search on trie.
# Track the index of the next char to match in word and number of mistmatches seen so far. For each char, move down
# the trie to all children incrementing the mismatches if then node is different from the char of the word. Terminate
# at either the end fo the word or too many mismatches are found.
# Time - O(n) to buildDict where n is the total number of chars in all words in dictionary. O(m) to search where m is
# the length of the word since there are a finite number (25) of mismatches at every node.
# Space - O(n)

class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}      # key is char, value is dictionary

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        for word in dict:
            node = self.root

            for c in word:
                if c not in node:
                    node[c] = {}
                node = node[c]
            node["#"] = None  # signifies end of a word

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        def helper(i, mismatches, node):    # index of next char to match, nb mismatches

            if mismatches == 2:             # too many mismatches
                return False

            if i == len(word):              # end fo word, True if terminal node and 1 mismatch
                return "#" in node and mismatches == 1

            for c in node.keys():
                if c == "#":
                    continue
                if helper(i + 1, mismatches + (c != word[i]), node[c]):
                    return True

            return False

        return helper(0, 0, self.root)
