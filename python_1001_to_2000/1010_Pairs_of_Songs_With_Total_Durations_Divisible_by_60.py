_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/
# In a list of songs, the i-th song has a duration of time[i] seconds.
# Return the number of pairs of songs for which their total duration in seconds is divisible by 60.
# Formally, we want the number of indices i < j with (time[i] + time[j]) % 60 == 0.

# Count the number of songs with each (time modulo 60). For the songs with modulo time 0 and 30, we can form a pair of
# each song and each other song with the same time.
# For other times, we can form pairs of songs with time t and time 60 - t.
# Time - O(n)
# Space - O(1)

from collections import defaultdict

class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        mod_count = defaultdict(int)

        for t in time:
            mod_count[t % 60] += 1

        pairs = mod_count[0] * (mod_count[0] - 1) // 2
        pairs += mod_count[30] * (mod_count[30] - 1) // 2
        for t in range(1, 30):          # do not count to 60 to avoid double-counting
            pairs += mod_count[t] * mod_count[60 - t]

        return pairs
