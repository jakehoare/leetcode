_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/logger-rate-limiter/
# Design a logger system that receive stream of messages along with its timestamps, each message should be printed
# if and only if it is not printed in the last 10 seconds.
# Given a message and a timestamp (in seconds granularity), return true if the message should be printed in the
# given timestamp, otherwise returns false.
# It is possible that several messages arrive roughly at the same time.

# Dictionary maps messages to last print time. If message not sen before or not seen for 10 seconds then update last
# print time and return true. Else return false.
# Time - O(1)
# Space - O(n)

class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.last = {}

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        if message not in self.last or timestamp - self.last[message] >= 10:
            self.last[message] = timestamp
            return True

        return False