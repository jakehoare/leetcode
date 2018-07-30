_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/ambiguous-coordinates/
# We had some 2-dimensional coordinates, like "(1, 3)" or "(2, 0.5)".
# Then, we removed all commas, decimal points, and spaces, and ended up with the string S.
# Return a list of strings representing all possibilities for what our original coordinates could have been.
# Our original representation never had extraneous zeroes, so we never started with numbers like "00", "0.0", "0.00",
# "1.0", "001", "00.01", or any other number that can be represented with less digits.
# Also, a decimal point within a number never occurs without at least one digit occuring before it, so we never
# started with numbers like ".1".
# The final answer list can be returned in any order.
# Also note that all coordinates in the final answer have exactly one space between them (occurring after the comma.

# Split the coordinates into two non-zero pieces where the comma will be inserted. For each piece, calculate a list of
# all possible numbers with a digit.
# If number has leading and trailing zeros zero it can only be zero.
# If a number has a leading zero, it must have a decimal point after the zero.
# If a number has a trailing zero, it cannot have a decimal point.
# Else insert the decimal point in all possible places.
# Create all possible combinations of the left and right pieces.
# Time - O(n**4), O(n**3) possible coordinates
# Space - O(n**4)

class Solution(object):
    def ambiguousCoordinates(self, S):
        """
        :type S: str
        :rtype: List[str]
        """

        def insert_decimal(s):  # return list of possible representations of a number

            if s == "0":        # special case of leading and trailing zero
                return [s]
            if s[0] == "0" and s[-1] == "0":    # cannot have both leading and trailing zeros
                return []
            if s[0] == "0":     # cannot have multiple leading zeros before decimal point
                return ["0." + s[1:]]
            if s[-1] == "0":    # cannot have any trailing zeros after decimal point
                return [s]

            return [s[:i] + "." + s[i:] for i in range(1, len(s))] + [s]

        S = S[1:-1]             # remove brackets
        result = []

        for i in range(1, len(S)):  # insert comma after index i

            left = insert_decimal(S[:i])
            right = insert_decimal(S[i:])
            result += ["(" + ", ".join([l, r]) + ")" for l in left for r in right]

        return result
