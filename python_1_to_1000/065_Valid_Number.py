_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/valid-number/
# Validate if a given string is numeric.
# Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one.

# Test if integer or float or scientific.  Allow for first character signs.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def isNumber(self, s):
        self.digits = {str(i) for i in range(10)}
        s = [c for c in s.strip().lower()]
        if not s:
            return False
        return self.is_int(s, True) or self.is_float(s) or self.is_sci(s)


    def is_int(self, s, signed):
        if len(s) == 0:
            return False
        if s[0] == '-' and signed:
            s = s[1:]
        elif s[0] == '+' and signed:
            s = s[1:]
        if len(s) == 0:
            return False

        for c in s:
            if c not in self.digits:
                return False
        return True


    def is_float(self, s):
        try:
            dot = s.index('.')
            before = s[:dot]
            after = s[dot+1:]

            if before and before[0] in '+-':
                before = before[1:]
            if before and not self.is_int(before, False):
                return False
            if after and not self.is_int(after, False):
                return False
            return before or after
        except:
            return False


    def is_sci(self, s):
        try:
            e = s.index('e')
            before = s[:e]
            after = s[e+1:]

            if not before or not after:
                return False
            if not self.is_int(before, True) and not self.is_float(before):
                return False
            return self.is_int(after, True)
        except:
            return False