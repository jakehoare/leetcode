_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/generalized-abbreviation/
# Write a function to generate the generalized abbreviations of a word.
# Example: Given word = "word", return the following list (order does not matter):
# ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]

# For each letter, either abbreviate that letter by converting it to an integer and possibly adding to the count of
# previously abbreviated letters, or do not abbreviate and leave the letter as it is.
# Time - O(2**n)
# Space - O(n * 2**n)

class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        abbreviations = [[]]

        for c in word:
            new_abbreviations = []
            for abbr in abbreviations:

                # abbreviate c
                if len(abbr) > 0 and isinstance(abbr[-1], int):
                    new_abbreviations.append(abbr[:-1] + [abbr[-1] + 1])
                else:
                    new_abbreviations.append(abbr + [1])

                # do not abbreviate c
                new_abbreviations.append(abbr + [c])

            abbreviations = new_abbreviations

        return ["".join(map(str, a)) for a in abbreviations]