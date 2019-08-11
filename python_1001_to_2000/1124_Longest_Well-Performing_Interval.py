_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/longest-well-performing-interval/
# We are given hours, a list of the number of hours worked per day for a given employee.
# A day is considered to be a tiring day if and only if the number of hours worked is (strictly) greater than 8.
# A well-performing interval is an interval of days for which the number of tiring days is strictly larger
# than the number of non-tiring days.
# Return the length of the longest well-performing interval.

# Iterate over hours, updating the net balance of tiring days.
# If the net balance is positive, the array so far is the longest well-performing interval.
# If there is a prefix array such that an intermediate array has a net balance of 1 tiring day, then update the result
# if this is an improvement.
# Update the mapping from index to the first occurrence of a net tiring balance.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def longestWPI(self, hours):
        """
        :type hours: List[int]
        :rtype: int
        """
        TIRING = 8

        result = 0
        net_tiring = 0          # balance of tiring - non-tiring days
        first_net_tiring = {}   # map the first occurrence of each net_tiring to its index in hours

        for i, day in enumerate(hours):
            net_tiring += 1 if day > TIRING else -1
            if net_tiring > 0:  # hours[:i + 1] is well-performing, must be best result
                result = i + 1

            if net_tiring - 1 in first_net_tiring:  # removing some prefix of hours leaves a net_tiring of 1
                result = max(result, i - first_net_tiring[net_tiring - 1])

            if net_tiring not in first_net_tiring:
                first_net_tiring[net_tiring] = i

        return result
