_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/
# In an infinite binary tree where every node has two children, the nodes are labelled in row order.
# In the odd numbered rows (ie., the first, third, fifth,...), the labelling is left to right,
# while in the even numbered rows (second, fourth, sixth,...), the labelling is right to left.

# We can mive up the tree to each parent by dividing by 2.
# But because alternate rows are reversed, this will give the correect answer for every other row.
# So find the position of the label if the row of the label is reversed and move up the tree alternately using
# the original and reversed labels.
# Time - O(log n)
# Space - O(log n)

class Solution(object):
    def pathInZigZagTree(self, label):
        """
        :type label: int
        :rtype: List[int]
        """
        power_of_2 = 1
        while power_of_2 <= label:
            power_of_2 *= 2

        a = label
        b = power_of_2 - label - 1 + power_of_2 // 2    # equivalent label in reversed row

        result = []
        while a != 1:           # until root
            result.append(a)
            a //= 2             # up to parents
            b //= 2
            a, b = b, a         # alternate reversed and not

        result.append(1)
        return result[::-1]     # start from root
