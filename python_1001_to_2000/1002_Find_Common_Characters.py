_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/find-common-characters/
# Given an array A of strings made only from lowercase letters, return a list of all characters that show up in
# all strings within the list (including duplicates).
# For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three
# times in the final answer.
# You may return the answer in any order.

# Count the frequency of each character in the first word. For each other word, set the count of each character to the
# lower of the existing character count and count in the other word.
# Time - O(mn) for m words of length n
# Space - O(mn)

from collections import Counter

class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        counts = Counter(A[0])

        for word in A[1:]:
            word_count = Counter(word)
            for c in counts:
                counts[c] = min(counts[c], word_count[c])

        result = []
        for char, count in counts.items():
            result += [char] * count        # append count copies of each char
        return result
