_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
# Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters,
# and removing them.
# We repeatedly make duplicate removals on S until we no longer can.
# Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.

# Iterate over s. When a char matches the previous retained char, discard the both. Else retain the char.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        result = []
        for c in S:
            if result and result[-1] == c:
                result.pop()
            else:
                result.append(c)

        return "".join(result)
