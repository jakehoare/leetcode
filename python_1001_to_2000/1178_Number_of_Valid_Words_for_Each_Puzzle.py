_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/number-of-valid-words-for-each-puzzle/
# With respect to a given puzzle string, a word is valid if both the following conditions are satisfied:
# word contains the first letter of puzzle.
# For each letter in word, that letter is in puzzle.
# For example, if the puzzle is "abcdefg", then valid words are "faced", "cabbage", and "baggage";
# while invalid words are "beefed" (doesn't include "a") and "based" (includes "s" which isn't in the puzzle).
# Return an array answer, where answer[i] is the number of words in the given word list words that are valid
# with respect to the puzzle puzzles[i].

# Convert each word to an integer, where a set bit indicates the presence of of a character.
# Count the frequency of each such integer.
# For each puzzle, form all combinations of integers from characters of the puzzle. Always include the first
# character + any number of other character. Add to the result the count of words with each combination.
# Time - O(mk + n * 2**p) for m words of length k, and n puzzles of length p.
# Space - O(mk + n)

from collections import Counter
from itertools import combinations

class Solution(object):
    def findNumOfValidWords(self, words, puzzles):
        """
        :type words: List[str]
        :type puzzles: List[str]
        :rtype: List[int]
        """
        def word_to_int(s):
            bits = 0
            for c in s:
                bits |= (1 << (ord(c) - ord("a")))
            return bits

        word_bits_counter = Counter(word_to_int(w) for w in words)

        result = []

        for puzzle in puzzles:
            first_char_bit = word_to_int(puzzle[0])                 # this bit is always set
            other_char_bits = [word_to_int(c) for c in puzzle[1:]]  # check all combinations of these bits
            valid = 0
            for k in range(7):                                      # 0 to 6 other bits
                for combination in combinations(other_char_bits, k):
                    valid += word_bits_counter[first_char_bit + sum(combination)]
            result.append(valid)

        return result


