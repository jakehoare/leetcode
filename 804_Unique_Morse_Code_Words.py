_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/unique-morse-code-words/
# International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes,
# as follows: "a" maps to ".-", "b" maps to "-...", "c" maps to "-.-.", and so on.
# Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter.
# For example, "cab" can be written as "-.-.-....-", (which is the concatenation "-.-." + "-..." + ".-").
# We'll call such a concatenation, the transformation of a word.
# Return the number of different transformations among all words we have.

# Create the transformation of each word as a list of the transformations of each letter.
# Create a set of all transformations.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        codes = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                 "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        morse = set()

        for word in words:

            transformation = []

            for c in word:
                transformation.append(codes[ord(c) - ord("a")])

            morse.add("".join(transformation))

        return len(morse)
