_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/
# There are n people whose IDs go from 0 to n - 1 and each person belongs exactly to one group.
# Given the array groupSizes of length n telling the group size each person belongs to,
# return the groups there are and the people's IDs each group includes.
# You can return any solution in any order and the same applies for IDs.
# Also, it is guaranteed that there exists at least one solution.

# Create a mapping of group size to its members.
# Iterate over the group sizes, adding each member to a group of the corresponding size.
# A new group is started if there is no group of the correct size.
# When a group has the correct number of members, add it to result and start a new empty group.
# Time - O(n)
# Space - O(n)

from collections import defaultdict

class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        size_to_group = defaultdict(list)
        result = []

        for i, size in enumerate(groupSizes):
            size_to_group[size].append(i)

            if len(size_to_group[size]) == size:    # group is full
                result.append(size_to_group[size])
                size_to_group[size] = []            # start a new group

        return result
