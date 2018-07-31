_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/most-common-word/
# Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.
# It is guaranteed there is at least one word that isn't banned, and that the answer is unique.
# Words in the list of banned words are given in lowercase, and free of punctuation.
# Words in the paragraph are not case sensitive. The answer is in lowercase.

# Split paragraph, convert words to lower case and remove punctuation. Count remaining word frequencies if not banned.
# Time - O(n) total length of all words + banned
# Space - O(n)

from collections import defaultdict

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        banned = set(banned)
        punct = {"!", "?", ",", ".", ";", "'"}
        counter = defaultdict(int)

        for word in (s.lower() for s in paragraph.split(" ")):
            word = "".join(c for c in word if c not in punct)
            if word not in banned:
                counter[word] += 1

        return max(counter.items(), key=lambda x: x[1])[0]  # key with max value


