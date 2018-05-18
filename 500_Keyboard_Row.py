_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/keyboard-row/
# Given a List of words, return the words that can be typed using letters of alphabet on only one row of a keyboard.

# Map each of the 26 keys to its row. Iterate over word, setting the row of the first char and checking that the rows
# of all other characters are the same as the first.
# Time - O(n) total number of characters in words.
# Space - O(1) excluding result.

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        keyboard = {}
        rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        for i, row in enumerate(rows):
            for c in row:
                keyboard[c] = i

        result = []

        for word in words:
            row = -1

            for c in word:
                if row == -1:                       # set the row of first char
                    row = keyboard[c.lower()]
                elif keyboard[c.lower()] != row:    # compare to previous rows
                    break
            else:
                result.append(word)

        return result
