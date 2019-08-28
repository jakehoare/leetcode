_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/longest-chunked-palindrome-decomposition/
# Return the largest possible k such that there exists a_1, a_2, ..., a_k such that:
# Each a_i is a non-empty string;
# Their concatenation a_1 + a_2 + ... + a_k is equal to text;
# For all 1 <= i <= k,  a_i = a_{k+1 - i}.

# Find a prefix of text that matches a suffix, then remove the prefix and the suffix and repeat.
# Continue until all the text is used or we are half way through and the middle is not a palindrome.
# Time - O(n**2)
# Space - O(n)

class Solution(object):
    def longestDecomposition(self, text):
        """
        :type text: str
        :rtype: int
        """
        n = len(text)
        start_prefix = 0
        result = 0

        while start_prefix <= (n - 1) // 2:     # until half of text
            for length in range(1, ((n - 2 * start_prefix) // 2) + 1):
                prefix = text[start_prefix:start_prefix + length]
                suffix = text[n - start_prefix - length:n - start_prefix]
                if prefix == suffix:
                    result += 2             # prefix and suffix are removed
                    start_prefix += length  # start of next prefix
                    break
            else:                           # middle of text, not a palindrome
                result += 1
                break

        return result
