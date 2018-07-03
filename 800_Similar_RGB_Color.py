_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/similar-rgb-color/
# In the following, every capital letter represents some hexadecimal digit from 0 to f.
# The red-green-blue color "#AABBCC" can be written as "#ABC" in shorthand.
# For example, "#15c" is shorthand for the color "#1155cc".
# Now, say the similarity between two colors "#ABCDEF" and "#UVWXYZ" is -(AB - UV)^2 - (CD - WX)^2 - (EF - YZ)^2.
# Given the color "#ABCDEF", return a 7 character color that is most similar to #ABCDEF,
# and has a shorthand (that is, it can be represented as some "#XYZ"

# Convert each pair of characters to integer and fins the absolute difference. If the absolute difference is less than
# or equal to 8 then it is optimal to duplicate the first char of the pair. Otherwise the first char is greater than
# the second, it is a shorter distance to decrement the first char. Else increment the first char.
# Time - O(1)
# Space - O(1)

class Solution(object):
    def similarRGB(self, color):
        """
        :type color: str
        :rtype: str
        """
        result = ["#"]

        for i in range(1, 6, 2):            # first char of each pair

            first, second = int(color[i], 16), int(color[i + 1], 16)    # convert hex to integer
            difference = first - second

            if abs(difference) <= 8:
                char = color[i]
            elif difference > 0:
                char = hex(first - 1)[2]    # decrement and convert back to hex
            else:                           # difference < 0
                char = hex(first + 1)[2]
            result.append(char * 2)

        return "".join(result)