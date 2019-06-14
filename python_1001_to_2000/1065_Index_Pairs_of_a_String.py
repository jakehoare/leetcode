_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/index-pairs-of-a-string/
# Given a text string and words (a list of strings), return all index pairs [i, j]
# so that the substring text[i]...text[j] is in the list of words.

# Repeatedly find each word in text until it is not found.
# Start each find from the character after the previous find.
# Time - O(mn log mn) for m words in text of length n
# Space - O(mn)

class Solution(object):
    def indexPairs(self, text, words):
        """
        :type text: str
        :type words: List[str]
        :rtype: List[List[int]]
        """
        result = []
        for word in words:
            i = -1
            while True:
                i = text.find(word, i + 1)
                if i == -1:
                    break
                result.append([i, i + len(word) - 1])

        return sorted(result)
