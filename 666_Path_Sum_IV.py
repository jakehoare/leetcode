_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/path-sum-iv/
# If the depth of a tree is smaller than 5, then this tree can be represented by a list of three-digits integers.
# For each integer in this list:
# The hundreds digit represents the depth D of this node, 1 <= D <= 4.
# The tens digit represents the position P of this node in the level it belongs to, 1 <= P <= 8. The position is the
# same as that in a full binary tree.
# The units digit represents the value V of this node, 0 <= V <= 9.
# Given a list of ascending three-digits integers representing a binary with the depth smaller than 5. You need to
# return the sum of all paths from the root towards the leaves.

# Create a mapping from each node's location to its value. Location is a tuple (depth, pos) where pos is indexed
# from zero. Then recursively explore the tree from the root with depth-first search. If node has no children then
# it is a leaf so return partial sum (including own value). Else return sums of paths via left and right subtrees.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def pathSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mapping = {}                        # key is (depth, pos) of node, value is val

        for num in nums:
            location, val = divmod(num, 10)
            depth, pos = divmod(location, 10)
            mapping[(depth, pos - 1)] = val

        def sum_paths(location, partial):   # returns sum of all paths to leaves given partial sum so far from root

            if location not in mapping:
                return 0

            depth, pos = location
            new_partial = partial + mapping[location]
            left = (depth + 1, 2 * pos)
            right = (depth + 1, 2 * pos + 1)

            if left not in mapping and right not in mapping:    # leaf node
                return new_partial
            return sum_paths((depth + 1, 2 * pos), new_partial) + sum_paths((depth + 1, 2 * pos + 1), new_partial)

        return sum_paths((1, 0), 0)
