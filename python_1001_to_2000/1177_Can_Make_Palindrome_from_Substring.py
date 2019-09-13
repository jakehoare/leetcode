_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/can-make-palindrome-from-substring/
# Given a string s, we make queries on substrings of s.
# For each query queries[i] = [left, right, k], we may rearrange the substring s[left], ..., s[right],
# and then choose up to k of them to replace with any lowercase English letter.
# If the substring is possible to be a palindrome string after the operations above, the result of the query is true.
# Otherwise, the result is false.
# Return an array answer[], where answer[i] is the result of the i-th query queries[i].
# Note that: Each letter is counted individually for replacement so if for example s[left..right] = "aaa",
# and k = 2, we can only replace two of the letters.
# Also, note that the initial string s is never modified by any query.

# For each prefix of s, create an integer with a bit set for every char in the prefix that has an odd count.
# For each query, find the integers for the left and right + 1 prefixes.
# Count the number of chars in the query that have an odd number of bits set. These chars need to be changed to
# make a palindrome, apart from the central char if the query is of odd length.
# Time - O(m + n) where m is len(s) and there are n queries.
# Space - O(n)

class Solution(object):
    def canMakePaliQueries(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        char_odd_bits = [0]
        for c in s:
            char_odd_bits.append(char_odd_bits[-1] ^ (1 << ord(c) - ord("a")))

        result = []
        for left, right, k in queries:
            left_odd_bits = char_odd_bits[left]
            right_odd_bits = char_odd_bits[right + 1]
            odd_chars = bin(left_odd_bits ^ right_odd_bits).count("1")  # XOR to count different bits in left and right

            odd_chars -= (right - left + 1) % 2     # use an odd char for the middle if substring length is odd
            odd_chars -= 2 * k                      # change each odd char to match another odd char
            result.append(odd_chars <= 0)

        return result
