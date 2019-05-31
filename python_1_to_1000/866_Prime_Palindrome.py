_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/prime-palindrome/
# Find the smallest prime palindrome greater than or equal to N.
# Recall that a number is prime if it's only divisors are 1 and itself, and it is greater than 1.
# For example, 2,3,5,7,11 and 13 are primes.
# Recall that a number is a palindrome if it reads the same from left to right as it does from right to left.
# For example, 12321 is a palindrome.

# Iterate through palindromes until we find one >= N and prime. For N of length n, build palindromes of length n if n
# is odd, else of length n + 1. Since 11 is the only even length prime palindromes, we only consider odd length
# candidates. Prime checking of x is by testing divisibility by all odd integers <= sqrt(x).
# Time - O(n)
# Space - O(log n)

class Solution(object):
    def primePalindrome(self, N):
        """
        :type N: int
        :rtype: int
        """
        def is_prime(x):
            if x < 2 or x % 2 == 0:                     # remove 0, 1 and even numbers
                return x == 2
            for i in range(3, int(x ** 0.5) + 1, 2):    # check odds <= sqrt(x)
                if x % i == 0:
                    return False
            return True

        if 8 <= N <= 11:                                # 11 is the only result with even number of digits
            return 11

        n = len(str(N))
        lhs = 10 ** (n // 2)                            # left side of candidate, including middle digit
        while True:
            candidate = int(str(lhs) + str(lhs)[-2::-1])    # will have odd length
            if candidate >= N and is_prime(candidate):
                return candidate
            lhs += 1