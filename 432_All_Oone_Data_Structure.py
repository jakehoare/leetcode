_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/all-oone-data-structure/
# Implement a data structure supporting the following operations:
# Inc(Key) - Inserts a new key with value 1. Or increments existing key by 1. Key is guaranteed to be non-empty string.
# Dec(Key) - If Key's value is 1, remove it from the data structure. Otherwise decrements an existing key by 1. If the
# key does not exist, this function does nothing. Key is guaranteed to be a non-empty string.
# GetMaxKey() - Returns one of the keys with maximal value. If no element exists, return an empty string "".
# GetMinKey() - Returns one of the keys with minimal value. If no element exists, return an empty string "".

# Create doubly linked list of blocks. Each block contains all the keys for a given value. Blocks are in value order.
# Also maintain a mapping from key to its block.
# Time - O(1), all operations
# Space - O(n)

class Block(object):
    def __init__(self, val=0):
        self.val = val
        self.keys = set()
        self.before = None
        self.after = None

    def remove(self):
        self.before.after = self.after
        self.after.before = self.before
        self.before, self.after = None, None

    def insert_after(self, new_block):
        old_after = self.after
        self.after = new_block
        new_block.before = self
        new_block.after = old_after
        old_after.before = new_block


class AllOne(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.begin = Block()  # sentinel
        self.end = Block()  # sentinel
        self.begin.after = self.end
        self.end.before = self.begin
        self.mapping = {}  # key to block

    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: void
        """
        if not key in self.mapping:  # find current block and remove key
            current_block = self.begin
        else:
            current_block = self.mapping[key]
            current_block.keys.remove(key)

        if current_block.val + 1 != current_block.after.val:  # insert new block
            new_block = Block(current_block.val + 1)
            current_block.insert_after(new_block)
        else:
            new_block = current_block.after

        new_block.keys.add(key)  # update new_block
        self.mapping[key] = new_block  # ... and mapping of key to new_block

        if not current_block.keys and current_block.val != 0:  # delete current block if not seninel
            current_block.remove()

    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: void
        """
        if not key in self.mapping:
            return

        current_block = self.mapping[key]
        del self.mapping[key]  # could use self.mapping.pop(key)
        current_block.keys.remove(key)

        if current_block.val != 1:
            if current_block.val - 1 != current_block.before.val:  # insert new block
                new_block = Block(current_block.val - 1)
                current_block.before.insert_after(new_block)
            else:
                new_block = current_block.before
            new_block.keys.add(key)
            self.mapping[key] = new_block

        if not current_block.keys:  # delete current block
            current_block.remove()

    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        if self.end.before.val == 0:
            return ""
        key = self.end.before.keys.pop()  # pop and add back to get arbitrary (but not random) element
        self.end.before.keys.add(key)
        return key

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        if self.begin.after.val == 0:
            return ""
        key = self.begin.after.keys.pop()
        self.begin.after.keys.add(key)
        return key


