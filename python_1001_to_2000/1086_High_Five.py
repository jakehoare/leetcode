_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/high-five/
# Given a list of scores of different students, return the average score of each student's top five scores
# in the order of each student's id.
# Each entry items[i] has items[i][0] the student's id, and items[i][1] the student's score.
# The average score is calculated using integer division.

# For each id, maintain a heap of the top 5 scores.
# Add each result to its heap, popping off a value if the heap has more 3 elements.
# Then take the average of each heap and sort by id.
# Time - O(n log n) since heap is of fixed size.
# Space - O(n)

from collections import defaultdict
import heapq

class Solution(object):
    def highFive(self, items):
        """
        :type items: List[List[int]]
        :rtype: List[List[int]]
        """
        TOP_SCORES = 5
        heaps = defaultdict(list)

        for id, score in items:
            if len(heaps[id]) < TOP_SCORES:
                heapq.heappush(heaps[id], score)
            else:
                heapq.heappushpop(heaps[id], score)

        result = [[id, sum(scores) // 5] for id, scores in heaps.items()]
        return sorted(result)
