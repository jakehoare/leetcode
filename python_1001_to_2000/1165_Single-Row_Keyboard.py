_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/single-row-keyboard/
# There is a special keyboard with all keys in a single row.
# Given a string keyboard of length 26 indicating the layout of the keyboard (indexed from 0 to 25),
# initially your finger is at index 0.
# To type a character, you have to move your finger to the index of the desired character.
# The time taken to move your finger from index i to index j is |i - j|.
# You want to type a string word. Write a function to calculate how much time it takes to type it with one finger.

# Map each char of keyboard to its index.
# For each char of word, find the distance from the current index to that char.
# The update the total distance moved and index.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def calculateTime(self, keyboard, word):
        """
        :type keyboard: str
        :type word: str
        :rtype: int
        """
        char_to_index = {c : i for i, c in enumerate(keyboard)}

        result, index = 0, 0
        for c in word:
            next_index = char_to_index[c]
            result += abs(next_index - index)
            index = next_index

        return result
