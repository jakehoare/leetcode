_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/design-hashmap/
# Design a HashMap without using any built-in hash table libraries.
# To be specific, your design should include these functions:
# put(key, value) : Insert a (key, value) pair into the HashMap. If the value already exists, update the value.
# get(key): Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
# remove(key) : Remove the mapping for the value key if this map contains the mapping for the key.

# Use a list of size 10000 becasue there are at most 10000 additions and so a reasonable number of collisions.
# Eech bucket of the list stores a list of [key, value] pairs where the key hashes to the bucket index.
# Time - O(1) average case
# Space - O(n)

class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 10000
        self.hashmap = [[] for _ in range(self.size)]

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """
        bucket, index = self.key_index(key)
        if index == -1:
            self.hashmap[bucket].append([key, value])
        else:
            self.hashmap[bucket][index][1] = value

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        bucket, index = self.key_index(key)
        return -1 if index == -1 else self.hashmap[bucket][index][1]

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        bucket, index = self.key_index(key)
        if index != -1:
            del self.hashmap[bucket][index]

    def hash_function(self, key):
        return key % self.size

    def key_index(self, key):           # return the bucket that a key belongs to and its index if present else -1
        bucket = self.hash_function(key)
        pairs = self.hashmap[bucket]
        for i in range(len(pairs)):
            if pairs[i][0] == key:
                return (bucket, i)
        return (bucket, -1)