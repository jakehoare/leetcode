_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/reconstruct-original-digits-from-english/
# Given a non-empty string containing an out-of-order English representation of digits 0-9, output the digits in
# ascending order.
# Input contains only lowercase English letters.
# Input is guaranteed to be valid and can be transformed to its original digits.

# Count the occurrences of letters that uniquely identify thier words (0, 2, 4, 6, 8). For other digits, count the
# occurences of a letter and subtract letters from digits already counted.
# Time - O(n)
# Space - O(1)

from collections import Counter

class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        digit_freq = [0] * 10
        letter_freq = Counter(s)
        #(letter to be counted, words already counted with this letter, digit)
        words = [("z", [], 0), ("w", [], 2), ("u", [], 4), ("x", [], 6), ("g", [], 8),
                 ("o", [0, 2, 4], 1), ("r", [0, 4], 3), ("f", [4], 5), ("v", [5], 7), ("i", [5, 6, 8], 9)]

        for letter, other_digits, digit in words:
            word_count = letter_freq[letter]
            for other_digit in other_digits:
                word_count -= digit_freq[other_digit]
            digit_freq[digit] = word_count

        result = []
        for digit, count in enumerate(digit_freq):
            result += [str(digit)] * count
        return "".join(result)

