_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/lru-cache/
# Design and implement a data structure for Least Recently Used cache. It should support the following operations:
# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity,
# it should invalidate the least recently used item before inserting a new item.

# Dictionary stores keys with values of nodes.  Nodes form double linked list containing key, value pairs. DLL is in
# order of use with least recent at head and most recent at tail.
# Time - O(1) to set and get
# Space - O(n)

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.head = Node(None, None)      # least recently used, remove at head
        self.tail = Node(None, None)      # most recently used, add and update at tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert(self, node):
        node.prev, self.tail.prev.next = self.tail.prev, node
        node.next, self.tail.prev = self.tail, node

    def remove_at_head(self):
        node = self.head.next
        node.next.prev = self.head
        self.head.next = self.head.next.next
        key = node.key
        del node
        return key

    def update(self, node):
        node.prev.next = node.next      # take out from existing position
        node.next.prev = node.prev
        self.insert(node)               # put back at tail



class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.queue = DLL()
        self.mapping = {}


    def get(self, key):
        """
        :rtype: int
        """
        if key not in self.mapping:
            return -1
        node = self.mapping[key]
        self.queue.update(node)
        return node.val


    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.mapping:         # update value and move node to tail
            node = self.mapping[key]
            node.val = value
            self.queue.update(node)
            return

        node = Node(key, value)         # else new key
        self.mapping[key] = node
        self.queue.insert(node)

        if self.capacity == 0:          # cache is full, eject oldest
            removed_key = self.queue.remove_at_head()
            del self.mapping[removed_key]
        else:                           # decrement capacity
            self.capacity -= 1
