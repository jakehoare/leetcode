_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/encode-and-decode-strings/
# Design an algorithm to encode a list of strings to a string.
# The encoded string is then sent over the network and is decoded back to the original list of strings.

# Prepend each string with its lenght and a special char '*'.  To decode, find the first '*', text before this is the
# length of the substring.  find() will always locate '*' after the length, never within a substring.
# Alternatively, prepend each string by its length as a string, padding string length with zeros to be a fixed number
# of characters.
# Alternatively, separate strings by a rare character surrounded by spaces eg ' # '.  Whenever '#' appears in a string
# duplicate it such that all even numbers of consecutive "#" are from original strings.
# Time - O(n)
# Space - O(n)

class Codec:
    def encode(self, strs):
        """Encodes a list of strings to a single string.
        :type strs: List[str]
        :rtype: str
        """
        encoding = []
        for s in strs:
            len_s = str(len(s))
            encoding.append(len_s)  # length as string
            encoding.append('*')    # delimiter '*'
            encoding.append(s)
        return "".join(encoding)

    def decode(self, s):
        """Decodes a single string to a list of strings.
        :type s: str
        :rtype: List[str]
        """
        decoding = []
        i = 0
        while i < len(s):
            j = s.find('*', i)          # '*' must be present if any remaining test
            len_substring = int(s[i:j])
            decoding.append(s[j+1:j+1+len_substring])
            i = j+1+len_substring
        return decoding