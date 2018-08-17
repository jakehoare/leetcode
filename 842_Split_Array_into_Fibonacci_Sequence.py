_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/split-array-into-fibonacci-sequence/
# Given a string S of digits, such as S = "123456579", we can split it into a Fibonacci-like sequence [123, 456, 579].
# Formally, a Fibonacci-like sequence is a list F of non-negative integers such that:
# 0 <= F[i] <= 2^31 - 1, (that is, each integer fits a 32-bit signed integer type);
# F.length >= 3;
# and F[i] + F[i+1] = F[i+2] for all 0 <= i < F.length - 2.
# Also, note that when splitting the string into pieces, each piece must not have extra leading zeroes,
# except if the piece is the number 0 itself.
# Return any Fibonacci-like sequence split from S, or return [] if it cannot be done.

# Try all possible lengths of starting number. Max starting number length is less than half the length of S to allow
# a sequence of at least 3 numbers. Try all possible lengths of second number, allowing for the remaining string to
# be at least as long as the longets of the 2 numbers. Attempt to build a sequence for the remainder of S given
# the first 2 numbers.
# Time - O(n**2)
# Space - O(n)

class Solution(object):
    def splitIntoFibonacci(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        MAX_NUM = 2 ** 31 - 1

        def helper(i, n1, n2):          # build sequence from S[i] onwards starting with n1 and n2

            fib = [n1, n2]

            while i < len(S):

                next_num = fib[-1] + fib[-2]
                if next_num > MAX_NUM:
                    return []
                next_str = str(next_num)
                if S[i:i + len(next_str)] != next_str:  # next_str must match the next part of S
                    return []
                fib.append(next_num)
                i += len(next_str)

            return fib

        for len1 in range(1, (len(S) + 1) // 2):

            if len1 > 1 and S[0] == "0":    # no leading zero unless zero
                return []
            n1 = int(S[:len1])
            if n1 > MAX_NUM:
                return []

            len2 = 1
            while len(S) - len1 - len2 >= max(len1, len2):

                if len2 > 1 and S[len1] == "0": # no leading zero unless zero
                    break
                n2 = int(S[len1:len1 + len2])
                if n2 > MAX_NUM:
                    break

                fibonacci = helper(len1 + len2, n1, n2)
                if fibonacci:
                    return fibonacci
                len2 += 1

        return []