_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/valid-word-square/
# Given a sequence of words, check whether it forms a valid word square.
# A sequence of words forms a valid word square if the kth row and column read the exact same string,
# where 0 ≤ k < max(numRows, numColumns).

# Make a square of same length sides by padding words with spaces. If any word is longer than the first word then
# it is longer than the corresponding column so not a valid square. Check each row against each column.
# Time - O(n**2)
# Space - O(n**2)

class Solution(object):
    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        if len(words) != len(words[0]):     # ensure the sides of the square have the same length
            return False

        n = len(words[0])

        for i, word in enumerate(words[1:], 1):
            m = len(word)
            if m > n:                       # no other word can be longer than first word
                return False
            words[i] += (n - m) * " "       # pad words with spaces to make complete square

        for i in range(n):
            for j in range(n):
                if words[i][j] != words[j][i]:
                    return False

        return True