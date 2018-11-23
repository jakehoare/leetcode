_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/knight-dialer/
# A chess knight can move 2 squares horizontal/vertical and one square vertical/horizontal.
# This time, we place our chess knight on any numbered key of a phone pad (indicated above),
# and the knight makes N-1 hops. Each hop must be from one key to another numbered key.
# Each time it lands on a key (including the initial placement of the knight),
# it presses the number of that key, pressing N digits total.
# How many distinct numbers can you dial in this manner?
# Since the answer may be large, output the answer modulo 10^9 + 7.

# Create a mapping of which digits can be reached from each digit.
# Store the count of distinct numbers ending with each digit.
# For each move, add the count of solutions ending with each digit to the count of solutions ending with each
# reachable next digit.
# Time - O(n) since there are 10 digits and so at most 10 reachable next digits.
# Space - O(1)

class Solution:
    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """
        can_reach = [[4, 6],        # can_reach[i] is the list of digits that can be reached from i
                     [6, 8],
                     [7, 9],
                     [4, 8],
                     [0, 3, 9],
                     [],
                     [0, 1, 7],
                     [2, 6],
                     [1, 3],
                     [2, 4]]

        counts = [1] * 10           # one distinct number ending with each digit
        for _ in range(N - 1):

            new_counts = [0] * 10

            for digit, count in enumerate(counts):
                for next_digit in can_reach[digit]:
                    new_counts[next_digit] += count

            counts = new_counts

        return sum(counts) % (10 ** 9 + 7)