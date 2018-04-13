_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/reverse-vowels-of-a-string/
# Write a function that takes a string as input and reverse only the vowels of a string.

# Start pointers from left adn right of s. Increment left pointer until a vowel is found. Decrement right pointer until
# a vowel is found. Swap vowels. If pointers meet, return result.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = {"a", "e", "i", "o", "u"}
        vowels |= {c.upper() for c in vowels}   # add upper case vowels
        s = [c for c in s]                      # convert to list of chars
        left, right = 0, len(s) - 1

        while left < right:

            while s[left] not in vowels:
                left += 1
                if left == right:
                    return "".join(s)

            while s[right] not in vowels:
                right -= 1
                if left == right:
                    return "".join(s)

            s[left], s[right] = s[right], s[left]   # swap
            left += 1
            right -= 1

        return "".join(s)