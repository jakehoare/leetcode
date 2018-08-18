_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/backspace-string-compare/
# Given two strings S and T, return if they are equal when both are typed into empty text editors.
# "#" means a backspace character.

# Start at the ends of both strings. Step backwards to find the next non-deleted chars in both strings. Increment the
# chars to be deleted when "#" is seen, else decrement the number of chars to be deleted.
# Time - O(max(m, n))
# Space - O(1)

class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        s_i, t_i = len(S) - 1, len(T) - 1

        def next_char(string, i):           # finds index of next char not deleted
            delete = 0
            while i >= 0 and (delete or string[i] == "#"):      # while more chars to be deleted
                delete = delete + 1 if string[i] == "#" else delete - 1
                i -= 1
            return i

        while True:

            s_i = next_char(S, s_i)
            t_i = next_char(T, t_i)

            if s_i == -1 and t_i == -1:     # both strings ended
                return True
            if s_i == -1 or t_i == -1:      # one string ended
                return False
            if S[s_i] != T[t_i]:            # chars do not match
                return False

            s_i -= 1                        # move to next chars
            t_i -= 1