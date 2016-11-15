_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/candy/
# There are N children standing in a line. Each child is assigned a rating value.
# You are giving candies to these children subjected to the following requirements:
# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# What is the minimum candies you must give?

# Find how many candies are required due to children on left and then on right.
# Result for each child is the higher of those values.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        left = [1 for _ in range(len(ratings))]     # default to 1 per child
        right = [1 for _ in range(len(ratings))]

        for i in range(1, len(ratings)):            # increase above previous child if greater rating
            if ratings[i] > ratings[i-1]:
                left[i] = left[i-1] + 1

        candies = left[-1]      # rightmost child not included in loop below
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:           # increase if greater rating
                right[i] = right[i+1] + 1
            candies += max(left[i], right[i])       # child gets higher of candies due to left and right

        return candies