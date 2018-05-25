_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/4-keys-keyboard/
# Imagine you have a special keyboard with the following keys:
# Key 1: (A): Print one 'A' on screen.
# Key 2: (Ctrl-A): Select the whole screen.
# Key 3: (Ctrl-C): Copy selection to buffer.
# Key 4: (Ctrl-V): Print buffer on screen appending it after what has already been printed.
# Now, you can only press the keyboard for N times (with the above four keys), find out the maximum numbers of 'A' you
# can print on screen.

# The maximum for a given N is either just by printing 'A' N times, or producing the maximum maxA(i) from i key presses,
# then using the remaining N - i to create maxA(i) * (N - i). N - i must be at least 4 to create at least one copy.
# In fact the optimal occurs when N - i is 4 or 5.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def maxA(self, N):
        """
        :type N: int
        :rtype: int
        """
        def helper(n):
            if n in memo:
                return memo[n]

            max_A = n       # press 'A' n times
            for i in range(max(n - 5, 0), n - 3):               # i + 1 print 'A' to make a base list
                max_A = max(max_A, helper(i) * (n - i - 1))     # then n - (i + 1) copies of the base list

            memo[n] = max_A
            return max_A

        memo = {}
        return helper(N)