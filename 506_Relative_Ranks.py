_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/relative-ranks/
# Given scores of N athletes, find their relative ranks and the people with the top three highest scores, who will be
# awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".

# Create a list of tuples of num and its index in nums. Sort descending by num. Iterate over list, setting result
# with medals for the first 3 then rank as a string for others.
# Time - O(n log n)
# Space - O(n)

class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        num_i = [(num, i) for i, num in enumerate(nums)]
        num_i.sort(reverse=True)

        result = [None for _ in range(len(nums))]
        medals = ["Gold", "Silver", "Bronze"]

        for rank, (_, i) in enumerate(num_i):
            if rank < 3:                                # best ranked 3 get medals
                result[i] = medals[rank] + " Medal"
            else:
                result[i] = str(rank + 1)               # add 1 since enumeration is from zero

        return result
