_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/most-frequent-subtree-sum/
# Given the root of a tree, you are asked to find the most frequent subtree sum. The subtree sum of a node is defined
# as the sum of all the node values formed by the subtree rooted at that node (including the node itself). So what is
# the most frequent subtree sum value? If there is a tie, return all the values with the highest frequency in any order.

# Bottom-up recursion finding sum for each each subtree and adding to counter. Find max value of counter then find
# all keys with max value.
# Time - O(n)
# Space - O(n)

from collections import defaultdict

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        def count_sums(node):
            if not node:
                return 0

            total_sum = node.val + count_sums(node.left) + count_sums(node.right)
            tree_sums[total_sum] += 1

            return total_sum

        if not root:
            return []
        tree_sums = defaultdict(int)
        count_sums(root)

        max_sum = max(tree_sums.values())
        result = []
        for key, val in tree_sums.items():
            if val == max_sum:
                result.append(key)
        return result