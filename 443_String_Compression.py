_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/string-compression/
# Given an array of characters, compress it in-place.
# The length after compression must always be smaller than or equal to the original array.
# Every element of the array should be a character (not int) of length 1.
# After you are done modifying the input array in-place, return the new length of the array.

# Iterate over chars, finding when a sequence ends. Add the char to result and if the sequence is longer than 1 char
# then we compress and add the digits of the number of chars to the result.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        chars += " "            # append with ASCII value 32, will not appear in chars
        char_start = 0          # start index of sequence of current char
        result_length = 0       # next index for result to be updated

        for i, c in enumerate(chars):

            if c != chars[char_start]:      # not extending same sequence of chars

                chars[result_length] = chars[char_start]    # add this char to result
                result_length += 1

                seq_length = i - char_start

                if seq_length > 1:          # can compress
                    digits = list(str(seq_length))
                    digits_length = len(digits)
                    chars[result_length:result_length + digits_length] = digits # insert digits
                    result_length += digits_length

                char_start = i

        return result_length

