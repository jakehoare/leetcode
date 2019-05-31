_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/count-different-palindromic-subsequences/
# Given a string S, find the number of different non-empty palindromic subsequences in S, and return that number
# modulo 10^9 + 7.
# A subsequence of a string S is obtained by deleting 0 or more characters from S.
# A sequence is palindromic if it is equal to the sequence reversed.
# Two sequences A_1, A_2, ... and B_1, B_2, ... are different if there is some i for which A_i != B_i.

# Top-down dynamic programming. Precompute tables of the first of each char before and after each index (inclusive).
# Calculate the solution as the number of unique character + for each character x the number of palindromes of the
# form x_x where _ is any other palindrome. Memoise results.
# Time - O(n**2)
# Space - O(n**2)

class Solution(object):
    def countPalindromicSubsequences(self, S):
        """
        :type S: str
        :rtype: int
        """
        NUM_LETTERS, MOD = 4, 10 ** 9 + 7
        S = [ord(c) - ord("a") for c in S]                  # convert chars to integers
        memo = {}

        last_indices = [-1 for _ in range(NUM_LETTERS)]
        prev_index_letter = [None for _ in
                             range(len(S))]                 # prev_index_letter[i][j] is the previous occurrence of letter j
        for i in range(len(S)):                             # at or before index i
            last_indices[S[i]] = i
            prev_index_letter[i] = last_indices[:]

        last_indices = [-1 for _ in range(NUM_LETTERS)]
        next_index_letter = [None for _ in range(len(S))]   # next_index_letter[i][j] is the next occurrence of letter j
        for i in range(len(S) - 1, -1, -1):                 # at or after index i
            last_indices[S[i]] = i
            next_index_letter[i] = last_indices[:]

        def helper(i, j):                                   # solution for S[i:j + 1]

            if (i, j) in memo:
                return memo[(i, j)]

            count = 1                                       # empty string plus single characters

            for letter in range(4):
                next_index = next_index_letter[i][letter]   # first occurrence of letter after or including index i
                prev_index = prev_index_letter[j][letter]   # next occurrence of letter before or including index j

                if i <= next_index <= j:                    # single character palindromes
                    count += 1

                if next_index != -1 and prev_index != -1 and prev_index > next_index:   # string contains x_x
                    count += helper(next_index + 1, prev_index - 1)

            count %= MOD
            memo[(i, j)] = count
            return count

        return helper(0, len(S) - 1) - 1                    # remove empty string