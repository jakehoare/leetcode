_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/divide-chocolate/
# You have one chocolate bar that consists of some chunks.
# Each chunk has its own sweetness given by the array sweetness.
# You want to share the chocolate with your K friends so you start cutting the chocolate bar into K+1
# pieces using K cuts, each piece consists of some consecutive chunks.
# Being generous, you will eat the piece with the minimum total sweetness and give the other pieces to your friends.
# Find the maximum total sweetness of the piece you can get by cutting the chocolate bar optimally.

# Binary search the range of possible results.
# For each guess, check whether it is possible to split the bar into at least K pieces with each piece having at
# least guess sweetness.
# If it is possible, the guess is the new lower bound, ele the new upper bound is less than guess.
# Time - O(n log m) for n pieces and m total sweetness
# Space - O(1)

class Solution(object):
    def maximizeSweetness(self, sweetness, K):
        """
        :type sweetness: List[int]
        :type K: int
        :rtype: int
        """
        K += 1                                  # add piece for myself
        left, right = 1, sum(sweetness) // K    # possible result bounds (inclusive)

        def can_split(x):           # can split into >= K pieces with at least x sweetness per piece?
            piece, count = 0, 0
            for sweet in sweetness:
                piece += sweet
                if piece >= x:
                    count += 1
                    piece = 0

            return count >= K

        while left < right:
            mid = (left + right + 1) // 2
            if can_split(mid):
                left = mid
            else:
                right = mid - 1

        return left
