_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/invalid-transactions/
# A transaction is possibly invalid if:
# the amount exceeds $1000, or;
# if it occurs within (and including) 60 minutes of another transaction with the same name in a different city.
# Each transaction string transactions[i] consists of comma separated values representing:
# the name, time (in minutes), amount, and city of the transaction.
# Given a list of transactions, return a list of transactions that are possibly invalid.
# You may return the answer in any order.

# Sort all transactions by ascending time.
# For user, maintain an ordered list of previous transactions.
# For each transactions, add to result if cost > 1000.
# Iterate backwards through the previous transactions for that user, while they are within 60 minutes.
# If a previous transaction is in a different city, add both current and previous to the invalid set.
# Time - O(n**2) since for each transaction we may iterate through all previous transactions.
# Space - O(n)

from collections import defaultdict

class Solution(object):
    def invalidTransactions(self, transactions):
        """
        :type transactions: List[str]
        :rtype: List[str]
        """
        elements = [transaction.split(",") + [i] for i, transaction in enumerate(transactions)]
        elements.sort(key=lambda x: int(x[1]))      # sort by ascending time

        user_transactions = defaultdict(list)       # map user to list of transactions ordered by time
        invalid = set()                             # remove duplicates by using set

        for transaction in elements:
            name, time, cost, city, i = transaction
            time = int(time)

            if int(cost) > 1000:
                invalid.add(transactions[i])

            j = len(user_transactions[name]) - 1
            while j >= 0 and time - user_transactions[name][j][0] <= 60:    # while within 60 minutes
                if user_transactions[name][j][1] != city:
                    invalid.add(transactions[i])
                    invalid.add(transactions[user_transactions[name][j][2]])
                j -= 1

            user_transactions[name].append([time, city, i])     # update previous transactions for this person

        return list(invalid)
