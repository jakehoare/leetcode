_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/smallest-common-region/
# You are given some lists of regions where the first region of each list includes all other regions in that list.
# Naturally, if a region X contains another region Y then X is bigger than Y.
# Also by definition a region X contains itself.
# Given two regions region1, region2, find out the smallest region that contains both of them.
# If you are given regions r1, r2 and r3 such that r1 includes r3,
# it is guaranteed there is no r2 such that r2 includes r3.
# It's guaranteed the smallest region exists.

# Fins the intersection of the paths from each region to the root in the tree of regions.
# Create a mapping of each region to its parent.
# Starting from region 1, recursively move up the tree creating the set of parents.
# Then starting from region2, recursively find each parent and if it is in region1's path,
# this is the smallest common region.
# Time - O(n) for n regions.
# Space - O(n)

class Solution(object):
    def findSmallestRegion(self, regions, region1, region2):
        """
        :type regions: List[List[str]]
        :type region1: str
        :type region2: str
        :rtype: str
        """
        region_to_parent = {}

        for region_list in regions:
            parent = region_list[0]
            for region in region_list[1:]:
                region_to_parent[region] = parent

        region1_parents = [region1]
        while region1_parents[-1] in region_to_parent:
            region1_parents.append(region_to_parent[region1_parents[-1]])   # parent of last member of list

        region1_parents = set(region1_parents)

        while region2 not in region1_parents:
            region2 = region_to_parent[region2]

        return region2
