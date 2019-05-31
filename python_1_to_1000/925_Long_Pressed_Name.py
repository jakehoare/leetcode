_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/long-pressed-name/
# Your friend is typing his name into a keyboard.
# Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.
# You examine the typed characters of the keyboard.
# Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.

# For each char of name, count the run of identical chars. Count the run of the same char in typed. If there are more
# chars in name, it was not long pressed. Ensure all chars of typed have been accounted for.
# Time - O(m + n)
# Space - O(1)

class Solution:
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        typed_i, name_i = 0, 0              # indices of next char to check in each string

        while name_i < len(name):

            c, c_count = name[name_i], 1    # the char and the its count
            name_i += 1
            while name_i < len(name) and name[name_i] == c:         # count identical chars in name
                name_i += 1
                c_count += 1

            while typed_i < len(typed) and typed[typed_i] == c:     # count identical chars in typed
                typed_i += 1
                c_count -= 1

            if c_count > 0:                 # more in name than typed
                return False

        return typed_i == len(typed)        # must use all of typed