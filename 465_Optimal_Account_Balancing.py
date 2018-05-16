_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/optimal-account-balancing/
# A group of friends went on holiday and sometimes lent each other money. For example, Alice paid for Bill's lunch for
# $10. Then later Chris gave Alice $5 for a taxi ride. We can model each transaction as a tuple (x, y, z) which means
# person x gave person y $z. Assuming Alice, Bill, and Chris are person 0, 1, and 2 respectively (0, 1, 2 are the
# person's ID), the transactions can be represented as [[0, 1, 10], [2, 0, 5]].
# Given a list of transactions between a group of people, return the minimum number of transactions to settle the debt.

# Calculate the net balance owed to or from each person. For any sequence of net balances, calculate the number of
# transfers recursively. Take the net balance of the first person. If any other person has the opposite balance then
# net them off (one transfer) and calculate the transfers to settle the remaining balances. Else find the minimum
# transfers from netting with each other person.
# Time - O(m + (n - 1)!) where m = len(transactions) and n is the number of people, since t(n) = (n-1) * t(n-1)
# Space - O(n**2)

from collections import defaultdict

class Solution(object):
    def minTransfers(self, transactions):
        """
        :type transactions: List[List[int]]
        :rtype: int
        """
        balances = defaultdict(int)                 # map person to net balance
        for lender, receiver, amount in transactions:
            balances[lender] += amount
            balances[receiver] -= amount

        net_balances = [b for b in balances.values() if b != 0]

        def transfers(net_balances):

            if not net_balances:                    # base case
                return 0

            b = net_balances[0]
            for i in range(1, len(net_balances)):   # optimal to net exactly
                if b == -net_balances[i]:
                    return 1 + transfers(net_balances[1:i] + net_balances[i + 1:])

            min_transfers = float("inf")
            for i in range(1, len(net_balances)):
                if b * net_balances[i] < 0:         # opposite signs
                    count = 1 + transfers(net_balances[1:i] + net_balances[i + 1:] + [b + net_balances[i]])
                    min_transfers = min(min_transfers, count)

            return min_transfers

        return transfers(net_balances)