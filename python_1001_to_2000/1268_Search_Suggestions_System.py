_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/search-suggestions-system/
# Given an array of strings products and a string searchWord.
# We want to design a system that suggests at most three product names from products
# after each character of searchWord is typed.
# Suggested products should have common prefix with the searchWord.
# If there are more than three products with a common prefix return the three lexicographically minimums products.
# Return list of lists of the suggested products after each character of searchWord is typed.

# Sort the list of products.
# For each prefix of searchWord, binary search the list of products
# and add the list of the next 3 with the same prefix to the result.
# Time - O(n log n + k log n) for n products and searchWord of length k
# Space - O(n)

import bisect

class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        products.sort()
        results = []

        for length in range(1, len(searchWord) + 1):
            prefix = searchWord[:length]
            i = bisect.bisect_left(products, prefix)
            results.append([p for p in products[i: i + 3] if p[:length] == prefix])

        return results
