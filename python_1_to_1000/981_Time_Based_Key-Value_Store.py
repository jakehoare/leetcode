_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/time-based-key-value-store/
# Create a timebased key-value store class TimeMap, that supports two operations.
# 1. set(string key, string value, int timestamp)
# Stores the key and value, along with the given timestamp.
# 2. get(string key, int timestamp)
# Returns a value such that set(key, value, timestamp_prev) was called previously, with timestamp_prev <= timestamp.
# If there are multiple such values, it returns the one with the largest timestamp_prev.
# If there are no values, it returns the empty string ("").

# Two dictionaries map keys to a list of values and a list of times. Binary search the list of times to find the
# first index less than or equal to the required timestamp. If an index is found, lookup the value at that index.
# Time - O(1) for set, O(log n) for get
# Space - O(n)

from collections import defaultdict
import bisect

class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.key_to_values = defaultdict(list)
        self.key_to_times = defaultdict(list)

    def set(self, key: 'str', value: 'str', timestamp: 'int') -> 'None':
        self.key_to_values[key].append(value)
        self.key_to_times[key].append(timestamp)

    def get(self, key: 'str', timestamp: 'int') -> 'str':
        i = bisect.bisect_right(self.key_to_times[key], timestamp)
        if i == 0:
            return ""
        return self.key_to_values[key][i - 1]
