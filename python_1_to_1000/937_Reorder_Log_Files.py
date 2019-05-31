_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/reorder-log-files/
# You have an array of logs.  Each log is a space delimited string of words.
# For each log, the first word in each log is an alphanumeric identifier.  Then, either:
# Each word after the identifier will consist only of lowercase letters, or;
# Each word after the identifier will consist only of digits.
# We will call these two varieties of logs letter-logs and digit-logs.
# It is guaranteed that each log has at least one word after its identifier.
# Reorder the logs so that all of the letter-logs come before any digit-log.
# The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.
# The digit-logs should be put in their original order.
# Return the final order of the logs.

# For each log, find the first char after the space. If it is a digit, append to list of numbers logs.
# If it is a letter, create a tuple of the log with the identifier moved to the end and the original log.
# Sort the letter tuples and retain only the original logs in the solution.
# Time - O(kn log n) to sort n strings of maximum length k
# Space - O(nk)

class Solution:
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        letters, numbers = [], []
        digits = {str(i) for i in range(10)}

        for log in logs:
            space = log.find(" ")
            first = log[space + 1]
            if first in digits:
                numbers.append(log)
            else:
                letters.append((log[space + 1:] + log[:space], log))

        letters.sort()  # sort by log with identifier at end to break ties

        return [log for _, log in letters] + numbers