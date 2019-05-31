_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/text-justification/
# Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.
# Pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.
# Extra spaces between words should be distributed as evenly as possible.
# If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.
# For the last line of text, it should be left justified and no extra space is inserted between words.
# Each word is guaranteed not to exceed L in length.

# Fill lines with words and single spaces until full.  Then justify by distributing remaining spaces
# Time - O(maxWidth * nb_lines)
# Space - O(maxWidth * nb_lines)

class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        line_chars = 0          # number of chars on current line (without spaces)
        line_words = []         # list of words on current line
        justified = []          # output, list of justified strings

        for word in words:

            if line_chars + len(line_words) + len(word) <= maxWidth:    # add word to current line
                line_words.append(word)
                line_chars += len(word)

            else:                                   # word cannot be added to current line
                gaps = len(line_words) - 1          # nb gaps between words
                spaces = maxWidth - line_chars      # nb of spaces to make line maxWidth
                line = [line_words[0]]              # list of words and spaces
                if gaps == 0:                       # pad end if single word
                    line.append(" " * spaces)

                for line_word in line_words[1:]:    # distribute spaces between other words
                    space = spaces//gaps
                    if spaces % gaps != 0:          # round up if uneven division of spaces
                        space += 1
                    line.append(" " * space)        # add space
                    spaces -= space                 # reduce remaining spaces and gaps
                    gaps -= 1
                    line.append(line_word)

                justified.append("".join(line))

                line_words = [word]                 # add word to next line.
                line_chars = len(word)

        final_line = " ".join(line_words)           # pad final line with spaces
        final_line += " " * (maxWidth - len(final_line))
        justified.append(final_line)

        return justified
