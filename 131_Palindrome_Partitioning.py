_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/palindrome-partitioning/
# Given a string s, partition s such that every substring of the partition is a palindrome.
# Return all possible palindrome partitioning of s.

# If any prefix of s is a palindrome, then recursively partition the suffix into palindromes.
# Time - O(2**n), for string of length n there we can partition or not after each letter
# Space - O(2**n)

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        partitons = []
        self.find_partitions(s, [], partitons)
        return partitons


    def find_partitions(self, s, partial, partitions):
        if not s:
            partitions.append(partial)

        for i in range(1, len(s)+1):
            prefix = s[:i]
            if prefix == prefix[::-1]:
                self.find_partitions(s[i:], partial + [s[:i]], partitions)

