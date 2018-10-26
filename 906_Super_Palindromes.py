_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/super-palindromes/
# Let's say a positive integer is a superpalindrome if it is a palindrome, and it is also the square of a palindrome.
# Now, given two positive integers L and R (represented as strings), return the number of superpalindromes
# in the inclusive range [L, R].

# For all palindromes between sqrt(L) and sqrt(R), test if their square is a palindrome.
# Build ordered lists of palindromes of length x by surrounding all palindromes of length x - 2 with each digit.
# Palindromes that begin with 0 are built but not check if they are superpalindromes.
# Time - O(n log n)
# Max length of palindrome to check is k = log(R ** 0.5) = 0.5 * log R
# Number of palindromes of length <= k is O(10 ** ((k + 1) // 2)), each takes O(k) time to build and check if square is
# a super palindrome.
# Space - O(n log n)

class Solution(object):
    def superpalindromesInRange(self, L, R):
        """
        :type L: str
        :type R: str
        :rtype: int
        """
        L_sqrt = int(int(L) ** 0.5)
        R_sqrt = int((int(R) + 1) ** 0.5)
        digits = [str(i) for i in range(10)]

        def is_palindrome(i):
            return str(i) == str(i)[::-1]

        prev_palis, palis = [""], digits[:]         # palindromes with zero and one digit
        result = sum(L_sqrt <= i <= R_sqrt and is_palindrome(i ** 2) for i in range(10))

        for _ in range(2, 11):                      # gradually increase the palindrome length

            new_palis = []

            for digit in digits:
                for pal in prev_palis:              # palindromes of length - 2

                    new_pal = digit + pal + digit   # make new palindrome
                    new_palis.append(new_pal)

                    if new_pal[0] == "0":           # do not check if superpalindrome
                        continue

                    num = int(new_pal)

                    if num > R_sqrt:                # greater than maximum possible palindrome
                        return result

                    if L_sqrt <= num and is_palindrome(num ** 2):   # superpalindrome
                        result += 1

            prev_palis, palis = palis, new_palis