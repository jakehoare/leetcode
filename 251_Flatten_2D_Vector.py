_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/flatten-2d-vector/
# Implement an iterator to flatten a 2d vector.

# Store pointer to the next valid sublist and item.  To initialise and after every iteration move pointers to the next
# valid item or beyond final sublist.
# Time - O(1) for hasNext.  init() and next() are O(m) where m is number of sublists
# Space - O(n), total length of all sublists

class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.vec2d = vec2d
        self.list_nb, self.item_nb = 0, 0
        # while empty sublist, move to next sublist until end of vec2d
        while self.list_nb < len(self.vec2d) and len(self.vec2d[self.list_nb]) == 0:
            self.list_nb += 1

    def next(self):
        """
        :rtype: int
        """
        result = self.vec2d[self.list_nb][self.item_nb]
        if self.item_nb < len(self.vec2d[self.list_nb]) - 1:
            self.item_nb += 1   # not end of sublist, increment item
        else:                   # end of sublist, reset item and find next non-empty sublist or end of vec2d
            self.item_nb = 0
            self.list_nb += 1
            while self.list_nb < len(self.vec2d) and len(self.vec2d[self.list_nb]) == 0:
                self.list_nb += 1
        return result


    def hasNext(self):
        """
        :rtype: bool
        """
        return self.list_nb < len(self.vec2d)   # list_nb pointer beyond end of vec2d
