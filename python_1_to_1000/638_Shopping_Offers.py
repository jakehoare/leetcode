_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/shopping-offers/
# In LeetCode Store, there are some kinds of items to sell. Each item has a price.
# However, there are some special offers, and a special offer consists of one or more different kinds of items with
# a sale price.
# You are given the each item's price, a set of special offers, and the number we need to buy for each item.
# The job is to output the lowest price you have to pay for exactly certain items as given, where you could make
# optimal use of the special offers.
# Each special offer is represented in the form of an array, the last number represents the price you need to pay
# for this special offer, other numbers represents how many specific items you could get if you buy this offer.
# You could use any of special offers as many times as you want.

# Given a list of needs, find the cost of buying all items without special offers. Then for each special offer, if it
# does not involve more than needed of each item, use that offer and recurse.
# Space - O(n**m) where n is nb items and m is max nb of each item (nb tuples in memo)
# Time - O(kn * n**m) where k is nb specials. For each tuple, iterate over each item of each special.

class Solution(object):
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        def helper():

            needs_tuple = tuple(needs)
            if needs_tuple in memo:
                return memo[needs_tuple]

            min_cost = 0
            for cost, need in zip(price, needs):
                min_cost += need * cost
            if min_cost == 0:       # base case
                return 0

            for offer in special:
                for i, need in enumerate(needs):
                    if offer[i] > need:
                        break       # cannot use this offer
                else:
                    for i, need in enumerate(needs):
                        needs[i] -= offer[i]
                    min_cost = min(min_cost, offer[-1] + helper())
                    for i, need in enumerate(needs):
                        needs[i] += offer[i]

            memo[needs_tuple] = min_cost
            return min_cost


        memo = {}
        return helper()