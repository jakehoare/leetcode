_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/before-and-after-puzzle/
# Given a list of phrases, generate a list of Before and After puzzles.
# A phrase is a string that consists of lowercase English letters and spaces only.
# No space appears in the start or the end of a phrase. There are no consecutive spaces in a phrase.
# Before and After puzzles are phrases that are formed by merging two phrases where the last word of
# the first phrase is the same as the first word of the second phrase.
# Return the Before and After puzzles that can be formed by every two phrases phrases[i] and phrases[j] where i != j.
# Note that the order of matching two phrases matters, we want to consider both orders.
# You should return a list of distinct strings sorted lexicographically.

# Split all phrases by space.
# For each pair of split phrases, add to the result the concatenation if the last and first words are the same.
# Sort the result.
# Time - O(n**2 log n)
# Space - O(n**2)

class Solution(object):
    def beforeAndAfterPuzzles(self, phrases):
        """
        :type phrases: List[str]
        :rtype: List[str]
        """
        split_phrases = [phrase.split(" ") for phrase in phrases]
        result = set()          # eliminates duplicates

        for i, split_phrase1 in enumerate(split_phrases):
            for j, split_phrase2 in enumerate(split_phrases):
                if i != j and split_phrase1[-1] == split_phrase2[0]:
                    joined = " ".join(split_phrase1 + split_phrase2[1:])
                    result.add(joined)

        return sorted(result)
