_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/remove-outermost-parentheses/
# A valid parentheses string is either empty (""), "(" + A + ")", or A + B, where A and B are valid parentheses strings,
# and + represents string concatenation.
# For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
# A valid parentheses string S is primitive if it is nonempty, and there does not exist a way to split it into S = A+B,
# with A and B nonempty valid parentheses strings.
# Given a valid parentheses string S, consider its primitive decomposition: S = P_1 + P_2 + ... + P_k,
# where P_i are primitive valid parentheses strings.
# Return S after removing the outermost parentheses of every primitive string in the primitive decomposition of S.

# Maintain the net balance of opening - closing brackets. Iterate over S.
# If the balance is zero, we must have an opening bracket of a primitie string which is not added to the result.
# Update the balance and add the char to the result.
# Then if the balance is zero, we have a closing bracket of a primitive string, which is removed from the result.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        result = []
        balance = 0

        for c in S:

            if balance != 0:  # do not add opening bracket if all pairs are matched
                result.append(c)

            change = 1 if c == "(" else -1
            balance += change

            if balance == 0:  # remove closing bracket if all pairs are matched
                result.pop()

        return "".join(result)
