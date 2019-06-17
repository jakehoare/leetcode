_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/longest-duplicate-substring/
# Given a string S, consider all duplicated substrings: (contiguous) substrings of S that occur 2 or more times.
# The occurrences may overlap.
# Return any duplicated substring that has the longest possible length.
# If S does not have a duplicated substring, the answer is "".

# Binary search for the length of the longest repeated substring.
# For a given length guess, a repeated substring is found by taking the rolling hash of substrings of length guess.
# Rolling hash is calculated as C0 + C1 * MULTIPLIER + C2 * MULTIPLIER**2 + ... for characters C0, C1, ...
# Hash is also modulo MOD. Calculation of next hash as substring slides over S is O(1).
# Time - O(n log n)
# Space - O(n)

class Solution(object):
    def longestDupSubstring(self, S):
        """
        :type S: str
        :rtype: str
        """
        MOD = 2 ** 63 - 1
        MULTIPLIER = 26
        s = [ord(c) - ord("a") for c in S]  # convert char to integer

        def test(guess):                    # return index or None if no repeat
            hash_value = 0
            for i in range(guess):
                hash_value = (hash_value * MULTIPLIER + s[i]) % MOD

            val = (MULTIPLIER ** guess) % MOD
            seen = {hash_value}

            for i in range(guess, len(S)):
                hash_value = (hash_value * MULTIPLIER + s[i] - s[i - guess] * val) % MOD
                if hash_value in seen:
                    return i - guess + 1  # start index of duplicate
                seen.add(hash_value)

        result, low, high = 0, 0, len(S)
        while low < high:
            mid = (low + high + 1) // 2 # if high - low == 1, choose high
            index = test(mid)
            if index:                   # longest duplicate length is mid or greater
                low = mid
                result = index
            else:                       # longest duplicate length is less than mid
                high = mid - 1

        return S[result:result + low]
