_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/
# Design a data structure that supports all following operations in average O(1) time.
# Note: Duplicate elements are allowed.
# insert(val): Inserts an item val to the collection.
# remove(val): Removes an item val from the collection if present.
# getRandom: Returns a random element from current collection of elements. The probability of each element being
# returned is linearly related to the number of same value the collection contains.

# Maintain a list of vals and a mapping from val to all indices in list with that val.  To remove, replace in list
# with last val and update mapping of replacement.
# Time - O(1)
# Space - O(n)

from collections import defaultdict
import random


class RandomizedCollection(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.indices = defaultdict(set)  # value is the set of indices in self.nums with values of key

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        result = True
        if val in self.indices:
            result = False

        self.nums.append(val)
        self.indices[val].add(len(self.nums) - 1)
        return result

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.indices:
            return False

        i = self.indices[val].pop()     # remove any index with this val

        if not self.indices[val]:       # delete val from mapping
            del self.indices[val]

        if i == len(self.nums) - 1:     # only need to remove from list
            self.nums.pop()
        else:
            replacement = self.nums[-1]
            self.nums[i] = replacement
            self.nums.pop()
            self.indices[replacement].discard(len(self.nums))   # change index in replacement mapping
            self.indices[replacement].add(i)
        return True

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return self.nums[random.randint(0, len(self.nums) - 1)]