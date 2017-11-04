_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/add-bold-tag-in-string/
# Given a string s and a list of strings dict, you need to add a closed pair of bold tag <b> and </b> to wrap the
# substrings in s that exist in dict. If two such substrings overlap, you need to wrap them together by only one pair
# of closed bold tag. Also, if two substrings wrapped by bold tags are consecutive, you need to combine them.

# Create mapping of start letter to list of words in dictionary. Iterate over string, maintaining a list of words from
# dictionary that have partially matched s up to the current index. Matches list consist of previous matches that also
# match the next c, plus new words with he start letter of c. If all chars of a word are matched, mark all those chars
# in s as being in_tag. Finally, construct result by inserting opening and closing tags.
# Time - O(n * k * m), n words in dictionary of max length k, len(s) == m
# Space - O(nk + m)

from collections import defaultdict

class Solution(object):
    def addBoldTag(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        in_tag = [False for _ in range(len(s))]  # bool indicates whether char should be inside bold tag

        start_letters = defaultdict(list)       # mapping from start char to list of words with that start char
        for word in dict:
            start_letters[word[0]].append(word)

        matches = []                            # list of (word, word_index) that partially match s up word_index

        for i, c in enumerate(s):

            new_matches = []

            for word, word_index in matches:
                if c == word[word_index + 1]:
                    if word_index + 1 == len(word) - 1:     # end of word so mark range of in_tag
                        for j in range(i - len(word) + 1, i + 1):
                            in_tag[j] = True
                    else:
                        new_matches.append([word, word_index + 1])  # add to new list with next word_index

            for word in start_letters[c]:                   # words with first char == c
                if len(word) == 1:
                    in_tag[i] = True
                else:
                    new_matches.append([word, 0])

            matches = new_matches

        result = []
        for i, c in enumerate(s):

            if in_tag[i] and (i == 0 or not in_tag[i - 1]): # open tag
                result.append("<b>")
            elif not in_tag[i] and (i != 0 and in_tag[i - 1]):  # close tag
                result.append("</b>")

            result.append(c)

        if in_tag[-1]:
            result.append("</b>")   # final close tag
        return "".join(result)