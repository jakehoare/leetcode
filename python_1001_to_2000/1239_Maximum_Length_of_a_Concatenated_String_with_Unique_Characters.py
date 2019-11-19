_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
# Given an array of strings arr.
# String s is a concatenation of a sub-sequence of arr which have unique characters.
# Return the maximum possible length of s.

# Remove all words with duplicated letters and convert words to sets of letters.
# For each set of chars, check overlap with each previous result.
# If there is no overlap, append the combined char set to the previous results.
# Time - O(mn) for n words of length m, since length of dp is bounded by alphabet size.
# Space - O(n)

class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        char_sets = [set(s) for s in arr if len(s) == len(set(s))]
        dp = [set()]    # candidate resulting sets of chars after using each word

        for char_set in char_sets:
            for prev_char_set in dp[:]:
                combo = char_set | prev_char_set
                if len(combo) == len(char_set) + len(prev_char_set):
                    dp.append(combo)

        return max(len(char_set) for char_set in dp)

