_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/queue-reconstruction-by-height/
# Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k),
# where h is the height of the person and k is the number of people in front of this person who have a
# height greater than or equal to h. Write an algorithm to reconstruct the queue.

# Group people by height. Sort heights descending from tallest.  For each group of people of the same height, sort
# from least to most in front and insert into queue.  if_front is correct insertion position because there are no
# shorter people already in queue.
# Time - O(n**2), each person inserted into list.
# Space - O(n)

from collections import defaultdict

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        queue = []
        height_groups = defaultdict(list)

        for height, in_front in people:
            height_groups[height].append(in_front)

        all_heights = list(height_groups.keys())
        all_heights.sort(reverse = True)

        for height in all_heights:
            height_groups[height].sort()
            for in_front in height_groups[height]:
                queue.insert(in_front, [height, in_front])

        return queue