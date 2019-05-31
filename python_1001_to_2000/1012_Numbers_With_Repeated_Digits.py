_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/numbers-with-repeated-digits/
# Given a positive integer N, return the number of positive integers less than or equal to N that have at
# least 1 repeated digit.

# Count the numbers with repeated digits and subtract from N.
# Sum the counts with repeated digit for each power of 10 of length less than N+1.
# Then fix each digit in turn from the most significant and count the non-repeated numbers with fixed prefixes.
# Time - O(log n)
# Space - O(log n)

class Solution(object):
    def numDupDigitsAtMostN(self, N):
        """
        :type N: int
        :rtype: int
        """
        digits = [int(c) for c in str(N + 1)]   # convert N+1 to a list of digits
        n = len(digits)                         # length of N+1
        not_dup = 0                             # count of numbers without repeated digits

        # returns the number of permutations of length digits out of num_digits
        def permutations(num_digits, length):
            if length == 0:
                return 1
            # all perms of shorter length, extended by any unused digit
            return permutations(num_digits, length - 1) * (num_digits - length + 1)

        for i in range(1, n):                   # count not_dup for powers of 10 less than N
            # 9 possible leading digits (not zero) then permutations of the other 9 digits (including zero)
            not_dup += 9 * permutations(9, i - 1)

        seen = set()                            # previously fixed digits
        for i, max_digit in enumerate(digits):  # max_digit is the most significant unfixed digit of N+1
            for digit in range(0 if i else 1, max_digit):   # possible range of leading unfixed digit
                if digit not in seen:           # cannot use if digit has been fixed earlier
                    not_dup += permutations(9 - i, n - i - 1)   # perms of unused digit for shorter length
            if max_digit in seen:               # all future numbers will contain repeated max_digit
                break
            seen.add(max_digit)                 # fix this digit

        return N - not_dup
