_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/number-of-recent-calls/
# Write a class RecentCounter to count recent requests.
# It has only one method: ping(int t), where t represents some time in milliseconds.
# Return the number of pings that have been made from 3000 milliseconds ago until now.
# Any ping with time in [t - 3000, t] will count, including the current ping.
# It is guaranteed that every call to ping uses a strictly larger value of t than before.

# Add each time to a queue.
# Remove all previous times that are longer than 3000ms ago and return the length of the queue.
# Time - O(n) worst case for ping, O(1) on average.
# Space - O(n)

from collections import deque

class RecentCounter:

    def __init__(self):
        self.times = deque()
        self.WINDOW = 3000

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.times.append(t)
        while t - self.times[0] > self.WINDOW:
            self.times.popleft()

        return len(self.times)