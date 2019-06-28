_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/
# Return the lexicographically smallest subsequence of text that contains all the distinct characters
# of text exactly once.

# Map each char to its last index in text.
# Iterate over text. For each char, if it's in the text then ignore it.
# While the char is lexicographically after the top of stack and top of stack char also occurs later in text,
# then pop top of stack. Append char to stack and convert to string before returning.
# Time - O(n)
# Space - O(1) since alphabet size is limited.

class Solution(object):
    def smallestSubsequence(self, text):
        """
        :type text: str
        :rtype: str
        """
        last_index = {c: i for i, c in enumerate(text)}
        stack = []

        for i, c in enumerate(text):
            if c in stack:
                continue
            while stack and stack[-1] > c and last_index[stack[-1]] > i:
                stack.pop()
            stack.append(c)

        return "".join(stack)
