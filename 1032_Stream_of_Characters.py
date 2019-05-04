_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/stream-of-characters/
# Implement the StreamChecker class as follows:
# StreamChecker(words): Constructor, init the data structure with the given words.
# query(letter): returns true if and only if for some k >= 1, the last k characters queried
# (in order from oldest to newest, including this letter just queried) spell one of the words in the given list.

# Query is true if some word ends with the most recent query.
# Store the reversed words in a trie. Each node of the trie is a dictionary keyed by characters and with values of
# the child node corresponding to that character. The presence of a character of "#" indicates that a word terminates
# at that node. Also store the list of query characters.
# Add each query to list of previous query characters. Starting from the root of the trie, iterate backwards along the
# list of queries.
# If a character is not found, there is no word with the previous queries as a suffix.
# Return True if a complete word is found.
# Time - O(n) for __init__ where n is the total length of all words. O(m) to query where m is the number of queries.
# Space - O(m + n)

class StreamChecker(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.root = {}                  # Trie root, each node maps char to next node

        for word in words:
            node = self.root
            for c in reversed(word):
                if c not in node:
                    node[c] = {}
                node = node[c]
            node["#"] = True            # "#" signifies complete word

        self.queries = []

    def query(self, letter):
        """
        :type letter: str
        :rtype: bool
        """
        self.queries.append(letter)
        node = self.root

        for c in reversed(self.queries):
            if c not in node:
                return False
            node = node[c]
            if "#" in node:
                return True

        return False    # end of queries reached without matching a word
