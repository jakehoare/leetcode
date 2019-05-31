_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/binary-trees-with-factors/
# Given an array of unique integers, each integer is strictly greater than 1.
# We make a binary tree using these integers and each number may be used for any number of times.
# Each non-leaf node's value should be equal to the product of the values of it's children.
# How many binary trees can we make?  Return the answer modulo 10 ** 9 + 7.

# Sort the numbers in ascending order. For each num, try all previous nums as a left child and if we can find
# left child * right child == num then add to the count of trees with num as root each tree with all possible
# combinations of left and right subtrees.
# Time - O(n**2)
# Space - O(n)

from collections import Counter

class Solution(object):
    def numFactoredBinaryTrees(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        num_to_trees = Counter(A)       # initially each num is a tree, all nums are unique as per question
        A.sort()

        for i, num in enumerate(A):

            for left in A[:i]:
                right, remainder = divmod(num, left)
                if right <= 1:
                    break
                if remainder == 0 and right in num_to_trees:
                    num_to_trees[num] += num_to_trees[left] * num_to_trees[right]

        return sum(num_to_trees.values()) % MOD