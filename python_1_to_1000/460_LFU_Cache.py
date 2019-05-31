_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/lfu-cache/
# Design and implement a data structure for Least Frequently Used (LFU) cache.
# It should support the following operations: get and put.
# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity, it
# should invalidate the least frequently used item before inserting a new item. For the purpose of this problem, when
# there is a tie (i.e., two or more keys that have the same frequency), the least recently used key would be evicted.

# Maintain dict form key to value, dict from key to (freq, time), priority queue and set of keys to update in queue.
# For get and put existing key, do not update queue but add key to update set. For put when cache is full, update queue
# until top item does not need updating.
# Time - O(1) for get, O(k log k) for put
# Space - O(k)

import heapq

class LFUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.time = 0
        self.map = {}  # key to value
        self.freq_time = {}  # key to (freq, time)
        self.priority_queue = []  # (freq, time, key), only updated when new key is added
        self.update = set()  # keys that have been get/put since last new key was added

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        self.time += 1

        if key in self.map:
            freq, _ = self.freq_time[key]
            self.freq_time[key] = (freq + 1, self.time)
            self.update.add(key)
            return self.map[key]

        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.capacity <= 0:
            return

        self.time += 1
        if not key in self.map:

            if len(self.map) >= self.capacity:  # must remove least frequent from cache

                while self.priority_queue and self.priority_queue[0][2] in self.update:
                    # whilst (least frequent, oldest) needs to be updated, update it and add back to heap
                    _, _, k = heapq.heappop(self.priority_queue)
                    f, t = self.freq_time[k]
                    heapq.heappush(self.priority_queue, (f, t, k))
                    self.update.remove(k)

                # remove (least frequent, oldest)
                _, _, k = heapq.heappop(self.priority_queue)
                self.map.pop(k)
                self.freq_time.pop(k)

            self.freq_time[key] = (0, self.time)
            heapq.heappush(self.priority_queue, (0, self.time, key))

        else:
            freq, _ = self.freq_time[key]
            self.freq_time[key] = (freq + 1, self.time)
            self.update.add(key)

        self.map[key] = value
