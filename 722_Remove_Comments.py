_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/remove-comments/
# Given a C++ program, remove comments from it. The program source is an array where source[i] is the i-th line of the
# source code. This represents the result of splitting the original source code string by the newline character \n.
# In C++, there are two types of comments, line comments, and block comments.
# The string // denotes a line comment, which represents that it and rest of the characters to the right of it in the
# same line should be ignored.
# The string /* denotes a block comment, which represents that all characters until the next (non-overlapping)
# occurrence of */ should be ignored. (Here, occurrences happen in reading order: line by line from left to right.)
# To be clear, the string /*/ does not yet end the block comment, as the ending would be overlapping the beginning.
# The first effective comment takes precedence over others: if the string // occurs in a block comment, it is ignored.
# Similarly, if the string /* occurs in a line or block comment, it is also ignored.
# If a certain line of code is empty after removing comments, you must not output that line: each string in the answer
# list will be non-empty.
# There will be no control characters, single quote, or double quote characters. For example,
# source = "string s = "/* Not a comment. */";" will not be a test case. (Also, nothing else such as defines or macros
# will interfere with the comments.)
# It is guaranteed that every open block comment will eventually be closed, so /* outside of a line or block comment
# always starts a new comment.
# Finally, implicit newline characters can be deleted by block comments. Please see the examples below for details.
# After removing the comments from the source code, return the source code in the same format.

# Iterate over text, checking the string of the next 2 chars. Set comment_block according to opening and closing
# comments. At end of line, if not in a comment_block then add to result.
# Time - O(n), total number of chars
# Space - O(n)

class Solution(object):
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        removed = []
        comment_block = False
        new_line = []

        for line in source:
            i = 0

            while i < len(line):

                test = line[i:i + 2]
                if not comment_block and test == "/*":      # do not skip if in block to handle "/*/"
                    comment_block = True                    # else skip 2 chars
                    i += 2
                elif not comment_block and test == "//":    # skip to end of line
                    i = len(line)
                elif comment_block and test == "*/":        # end block, skip 2 chars
                    comment_block = False
                    i += 2
                elif comment_block:                         # ignore char
                    i += 1
                else:                                       # add char to result
                    new_line.append(line[i])
                    i += 1

            if not comment_block and new_line:              # newline char is not commented out
                removed.append("".join(new_line))
                new_line = []

        if new_line:                                        # add final text
            removed.append("".join(new_line))
        return removed

