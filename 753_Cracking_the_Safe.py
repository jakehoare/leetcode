_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/cracking-the-safe/
# There is a box protected by a password. The password is n digits, where each letter can be one of the first
# k digits 0, 1, ..., k-1.
# You can keep inputting the password, the password will automatically be matched against the last n digits entered.
# For example, assuming the password is "345", I can open it when I type "012345", but I enter a total of 6 digits.
# Please return any string of minimum length that is guaranteed to open the box after the entire string is inputted.

# Create a directed graph where each node is the last n-1 digits of the pattern used and each node has k outgoing edges
# each labeled by a digit such that node + edge represents a pattern (i.e. a password attempt).
# We need to find a Euler cycle that visits every edge of this graph.
# From a node, take each edge in turn and if pattern has not been seen already then explore from the next node with
# depth first search until we reach a dead end, which must be on the current cycle since each node has the same
# number of incoming and outgoing edges. Record the digit of the last edge in the result, then back-up within the cycle,
# taking alternative paths.
# Time - O(n * k**n) since k**n patterns each of length n
# Space - O(n * k**n)

class Solution(object):
    """
    :type n: int
    :type k: int
    :rtype: str
    """
    def crackSafe(self, n, k):

        seen = set()
        digits = [str(i) for i in range(k)]
        result = []

        def dfs(node):
            for x in digits:
                pattern = node + x
                if pattern not in seen:
                    seen.add(pattern)
                    dfs(pattern[1:])
                    result.append(x)

        dfs("0" * (n - 1))
        return "".join(result) + "0" * (n - 1)


sol = Solution()
print(sol.crackSafe(3, 2))
