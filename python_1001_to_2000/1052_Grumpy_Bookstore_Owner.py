_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/grumpy-bookstore-owner/
# Today, the bookstore owner has a store open for customers.length minutes.
# Every minute, some number of customers (customers[i]) enter the store, and all those customers
# leave after the end of that minute.
# On some minutes, the bookstore owner is grumpy.
# If the bookstore owner is grumpy on the i-th minute, grumpy[i] = 1, otherwise grumpy[i] = 0.
# When the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise they are satisfied.
# The bookstore owner knows a secret technique to keep themselves not grumpy for X minutes, but can only use it once.
# Return the maximum number of customers that can be satisfied throughout the day.

# Count the base case number of satisfied customers if the special technique is not used.
# Then for a sliding window of length X minutes, count the additional number of customers that can be satisfied.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def maxSatisfied(self, customers, grumpy, X):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type X: int
        :rtype: int
        """
        base_satisfied = 0
        window, best_window = 0, 0

        for i in range(len(customers)):
            if grumpy[i] == 1:
                window += customers[i]          # add additional customers to window
            else:
                base_satisfied += customers[i]

            if i - X >= 0 and grumpy[i - X] == 1:
                window -= customers[i - X]      # remove customers from window

            best_window = max(best_window, window)

        return base_satisfied + best_window
