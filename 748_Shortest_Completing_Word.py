_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/shortest-completing-word/
# Find the minimum length word from a given dictionary words, which has all the letters from the string licensePlate.
# Such a word is said to complete the given string licensePlate
# Here, for letters we ignore case. For example, "P" on the licensePlate still matches "p" on the word.
# It is guaranteed an answer exists. If there are multiple answers, return the one that occurs first in the array.
# The license plate might have the same letter occurring multiple times. For example, given a licensePlate of "PP",
# the word "pair" does not complete the licensePlate, but the word "supper" does.

# Count frequency fo each letter in licensePlate. Sort words in ascending order of length. For each word, count the
# frequency of each letter. If every letter in licensePlate has the same number or more copies in a word then return
# that word. Although sorting has worse time complexity, it is practically faster for the test cases than scanning the
# unsorted words.
# Time - O(kn log n) to sort for n log n comparisons, each taking O(k) for n strings of length k.
# Space - O(kn)

from collections import Counter

class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        letters = [c.lower() for c in licensePlate if c > "9"]  # remove digits and space
        freq = Counter(letters)

        words.sort(key=lambda x: len(x))

        for word in words:

            if len(word) < len(letters):                        # ignore words that are too short
                continue

            word_freq = Counter(word)

            for c, count in freq.items():
                if c not in word_freq or word_freq[c] < count:
                    break
            else:
                return word