_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/word-abbreviation/
# Given an array of n distinct non-empty strings, you need to generate minimal possible abbreviations for every word
# following rules below.
# Begin with the first character and then the number of characters abbreviated, which followed by the last character.
# If there are any conflict, that is more than one words share the same abbreviation, a longer prefix is used instead
# of only the first character until making the map from word to abbreviation become unique. In other words, a final
# abbreviation cannot map to more than one original words.
# If the abbreviation doesn't make the word shorter, then keep it as original.

# Create abbreviation for each word ignoring conflicts. Group words by abbreviation. If single word in group, retain
# abbreviation. Else recurse on group, creating new groups by next char until group lengths are 1 (which will always
# happen since words are unique).
# Time - O(nk) for n words of max length k
# Space - O(nk)

from collections import defaultdict

class Solution(object):
    def wordsAbbreviation(self, dictionary):
        """
        :type dict: List[str]
        :rtype: List[str]
        """

        def make_abbreviation(word, i):
            abbreviation = word[:i + 1] + str(len(word) - (i + 2)) + word[-1]
            return word if len(abbreviation) >= len(word) else abbreviation

        def abbreviate(group, prefix_end):  # prefix_end is last char of prefix
            new_groups = defaultdict(list)
            for i in group:
                new_groups[dictionary[i][prefix_end]].append(i)     # key is char, value is list of words
            for new_group in new_groups.values():
                if len(new_group) == 1:
                    abbreviations[new_group[0]] = make_abbreviation(dictionary[new_group[0]], prefix_end)
                else:
                    abbreviate(new_group, prefix_end + 1)

        n = len(dictionary)
        abbreviations = ["" for _ in range(n)]

        # group words by initial abbreviation
        groups = defaultdict(list)
        for i, word in enumerate(dictionary):
            groups[make_abbreviation(word, 0)].append(i)

        # iterate over groups
        for abbreviation, group in groups.items():
            if len(group) == 1:
                abbreviations[group[0]] = abbreviation
            else:
                abbreviate(group, 1)

        return abbreviations