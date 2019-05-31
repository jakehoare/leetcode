_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/map-sum-pairs/
# Implement a MapSum class with insert, and sum methods.
# For the method insert, you'll be given a pair of (string, integer). The string represents the key and the integer
# represents the value. If the key already existed, then the original key-value pair will be overridden to the new one.
# For the method sum, you'll be given a string representing the prefix, and you need to return the sum of all the
# pairs' value whose key starts with the prefix.

# Create a mapping from each prefix to the sum of vals of words with that prefix, and a separate mapping of vals of
# each words. If inserting a word which has been seen already, update the difference between the new an old val for
# all prefixes.
# Time - O(k**2) for insert and O(1) for sum
# Space - O(nk)

from collections import defaultdict

class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = defaultdict(int)        # map prefix to sum of vals with that prefix
        self.words = defaultdict(int)       # map whole words to their val

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        if key in self.words:               # update words and update val to change in val
            self.words[key], val = val, val - self.words[key]
        else:
            self.words[key] = val           # insert into words

        for i in range(len(key)):
            prefix = key[:i + 1]
            self.dict[prefix] += val        # update dict for all prefixes

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        return self.dict[prefix]