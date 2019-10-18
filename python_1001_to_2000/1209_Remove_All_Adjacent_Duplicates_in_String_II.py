_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/
# Given a string s, a k duplicate removal consists of choosing k adjacent and equal letters from s
# and removing them causing the left and the right side of the deleted substring to concatenate together.
# We repeatedly make k duplicate removals on s until we no longer can.
# Return the final string after all such duplicate removals have been made.
# It is guaranteed that the answer is unique.

# Maintain a stack of [char, count of identical chars in sequence].
# Iterate over s, updating the count of the top of stack if it's the same as the current char.
# If k chars are in sequence, pop them off the stack.
# If the current char is different from the top of stack, add the new char to stack with count of 1.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        stack = []      # stack of [char, sequence length]

        for c in s:
            if stack and stack[-1][0] == c:     # extend sequence of same char
                if stack[-1][1] == k - 1:       # remove sequence of k chars
                    stack.pop()
                else:
                    stack[-1][1] += 1
            else:
                stack.append([c, 1])

        return "".join(c * count for c, count in stack) # join remaining stack

