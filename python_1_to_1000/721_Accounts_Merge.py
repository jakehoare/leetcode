_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/accounts-merge/
# Given a list accounts, each element accounts[i] is a list of strings, where the first element accounts[i][0] is a
# name, and the rest of the elements are emails representing emails of the account.
# Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some email
# that is common to both accounts. Note that even if two accounts have the same name, they may belong to different
# people as people could have the same name. A person can have any number of accounts initially, but all of their
# accounts definitely have the same name.
# After merging the accounts, return the accounts in the following format: the first element of each account is the
# name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

# Create mapping from email to list of accounts with that email. For each account dfs to visit the accounts of its
# emails recursively.
# Time - O(n log n) where n is total number of emails. Each email visited once, then list sorted.
# Space - O(n)

from collections import defaultdict

class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        email_to_account = defaultdict(list)        # email to list of account indices containing that email

        for i, account in enumerate(accounts):
            for email in account[1:]:
                email_to_account[email].append(i)

        result = []
        visited = [False for _ in range(len(accounts))]

        def dfs(i):
            emails = set()
            if visited[i]:
                return emails
            visited[i] = True
            for email in accounts[i][1:]:
                emails.add(email)
                for account in email_to_account[email]:
                    emails |= dfs(account)          # union existing and new emails
            return emails

        for i, account in enumerate(accounts):
            emails = dfs(i)
            if emails:
                result.append([account[0]] + sorted(list(emails)))

        return result


