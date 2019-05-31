_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/goat-latin/
# A sentence S is composed of words separated by spaces. Each word consists of lowercase and uppercase letters only.
# We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.)
# The rules of Goat Latin are as follows:
# If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of the word.
# For example, the word 'apple' becomes 'applema'.
# If a word begins with a consonant (i.e. not a vowel), remove the first letter and append it to the end, then add "ma".
# For example, the word "goat" becomes "oatgma".
# Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
# For example, the first word gets "a" added to the end, the second word gets "aa" added to the end and so on.
# Return the final sentence representing the conversion from S to Goat Latin.

# Split by spaces. If a word does not start with a vowel, move first letter to end of word. Append word with "ma" and
# "a" according to index.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        S = S.split()
        vowels = {"a", "e", "i", "o", "u"}

        for i, word in enumerate(S):

            if word[0].lower() not in vowels:
                S[i] = S[i][1:] + S[i][0]

            S[i] += "ma" + "a" * (i + 1)

        return " ".join(S)