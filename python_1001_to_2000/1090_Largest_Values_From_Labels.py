_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/largest-values-from-labels/
# We have a set of items: the i-th item has value values[i] and label labels[i].
# Then, we choose a subset S of these items, such that:
# |S| <= num_wanted
# For every label L, the number of items in S with label L is <= use_limit.
# Return the largest possible sum of the subset S.

# Sort tuples of (value, label) in descending order.
# Greedily add each value to the result, provided do not add more than use_limit of each item.
# Track the remaining allowed number of each label in a dictionary.
# Return when we have added num_wanted values.
# Time - O(n log n)
# Space - O(n)

class Solution(object):
    def largestValsFromLabels(self, values, labels, num_wanted, use_limit):
        """
        :type values: List[int]
        :type labels: List[int]
        :type num_wanted: int
        :type use_limit: int
        :rtype: int
        """
        result, used = 0, 0
        remaining = {}      # map label to remaining number we can choose

        for value, label in sorted(zip(values, labels), reverse=True):
            remain = remaining.get(label, use_limit)    # default use_limit if not found
            if remain > 0:
                result += value
                remaining[label] = remain - 1
                used += 1
                if used == num_wanted:
                    break

        return result
