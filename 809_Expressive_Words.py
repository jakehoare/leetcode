_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/expressive-words/
# Sometimes people repeat letters to represent extra feeling, such as "hello" -> "heeellooo", "hi" -> "hiiii".
# Here, we have groups, of adjacent letters that are all the same character, and adjacent characters to the group
# are different.  A group is extended if that group is length 3 or more, so "e" and "o" would be extended in the
# first example, and "i" would be extended in the second example.
# As another example, the groups of "abbcccaaaa" would be "a", "bb", "ccc", and "aaaa"; and "ccc" and "aaaa" are the
# extended groups of that string.
# For some given string S, a query word is stretchy if it can be made to be equal to S by extending some groups.
# Formally, we are allowed to repeatedly choose a group (as defined above) of characters c, and add some number of the
# same character c to it so that the length of the group is 3 or more.
# Note that we cannot extend a group of size one like "h" to a group of size two like "hh" - all extensions must leave
# the group extended - ie., at least 3 characters long.
# Given a list of query words, return the number of words that are stretchy.

# Helper function get_groups returns the characters in a word and their group counts, in order.
# Compare the groups of S with groups of a word. All characters must match and each group cannot be larger in word and
# groups cannot be extended to be of length 2.
# Time - O(n) total length of all words and S.
# Space - O(s + t) where s = len(s) and t is the max length of any word.

from collections import namedtuple

class Solution(object):
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        Groups = namedtuple("groups", ["chars", "counts"])      # lists of chars and their counts

        def get_groups(word):                                   # make Groups for word

            groups = Groups(chars = [], counts = [])
            count = 1

            for i, c in enumerate(word):

                if i == len(word) - 1 or c != word[i + 1]:
                    groups.chars.append(c)
                    groups.counts.append(count)
                    count = 1
                else:
                    count += 1
            return groups

        result = 0
        S_groups = get_groups(S)

        for word in words:

            word_groups = get_groups(word)

            if word_groups.chars != S_groups.chars:         # all chars must match
                continue

            for S_count, word_count in zip(S_groups.counts, word_groups.counts):

                if word_count > S_count:                    # can only extend word groups
                    break
                if word_count < S_count and S_count == 2:   # cannot externd word group to be of length 2
                    break
            else:
                result += 1

        return result


s = "heeellooo"
test = ["hello", "hi", "helo"]
sol = Solution()
print(sol.expressiveWords(s, test))