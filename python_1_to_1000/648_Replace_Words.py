_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/replace-words/
# In English, we have a concept called root, which can be followed by some other words to form another longer word -
# let's call this word successor. For example, the root an, followed by other, which can form another word another.
# Now, given a dictionary consisting of many roots and a sentence. You need to replace all the successor in the
# sentence with the root forming it. If a successor has many roots can form it, replace it with the root with the
# shortest length.. You need to output the sentence after the replacement.

# Create a trie where each letter of a word maps to the next letter, terminating in the word. Insert all words of
# dictionary into trie. Terminate without inserting if perfix of a word is longer than a word already in trie.
# for each word in sentence, traverse through trie until no more nodes or word is found.
# Time - O(m + n) total number of chars in dictionary and sentence.
# Space - O(m) number of chars in dictionary

class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        result = []
        root = {}

        for word in dict:
            node = root
            for c in word[:-1]:
                if c not in node:   # create a new mapping
                    node[c] = {}
                elif isinstance(node[c], str):  # longer than an existing word
                    break
                node = node[c]
            else:
                node[word[-1]] = word           # terminate with word

        sentence = sentence.split(" ")
        for word in sentence:
            node = root
            for c in word:
                if c not in node:
                    result.append(word)         # no replacements
                    break
                if isinstance(node[c], str):    # replacement found
                    result.append(node[c])
                    break
                node = node[c]
            else:
                result.append(word)

        return " ".join(result)