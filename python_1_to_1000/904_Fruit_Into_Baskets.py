_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/fruit-into-baskets/
# In a row of trees, the i-th tree produces fruit with type tree[i].
# You start at any tree of your choice, then repeatedly perform the following steps:
# Add one piece of fruit from this tree to your baskets.  If you cannot, stop.
# Move to the next tree to the right of the current tree.  If there is no tree to the right, stop.
# Note that you do not have any choice after the initial choice of starting tree: you must perform step 1,
# then step 2, then back to step 1, then step 2, and so on until you stop.
# You have two baskets, and each basket can carry any quantity of fruit, but you want each basket to only carry
# one type of fruit each.
# What is the total amount of fruit you can collect with this procedure?

# The problem is to find the longest contiguous subarray containing only 2 different elements.
# For the 2 fruits in baskets, store the fruit and their first and last indices in the subarray.
# For each new fruit there are 5 cases:
# No previous fruits - set prev
# Only one previous fruit - swap prev to other and update prev and the result
# Fruit same as prev - update last index of prev and result
# Fruit same as other - update last index of prev, swap prev and other and update result
# Different fruit - replace other with prev and start index after the end index of other
# Time - O(n)
# Space - O(1)

class Solution:
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        prev = [None, float("inf"), float("inf")]   # [fruit, first_i, last_i]
        other = [None, float("inf"), float("inf")]

        result = 1

        for i, fruit in enumerate(tree):

            if fruit == prev[0]:
                prev[2] = i
                result = max(result, i + 1 - min(prev[1], other[1]))

            elif fruit == other[0]:
                other[2] = i
                other, prev = prev, other
                result = max(result, i + 1 - min(prev[1], other[1]))

            elif prev[0] is None:
                prev = [fruit, i, i]

            elif other[0] is None:
                other, prev = prev, [fruit, i, i]
                result = max(result, i + 1 - other[1])

            else:
                other = [prev[0], other[2] + 1, prev[2]]
                prev = [fruit, i, i]

        return result
