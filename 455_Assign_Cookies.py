_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/assign-cookies/
# Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at
# most one cookie. Each child i has a greed factor gi, which is the minimum size of a cookie that the child will be
# content with; and each cookie j has a size sj. If sj >= gi, we can assign the cookie j to the child i, and the
# child i will be content. Your goal is to maximize the number of your content children and output the maximum number.

# Sort both lists in ascending order. For each cookie, offer it to the next child. If it is accepted, increment the
# number of satisfied children and move to the next child. If it is not accepted, discard the cookie and test the
# next cookie on the same child.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        content = 0         # number of content children
        child = 0           # index of next child
        g.sort()
        s.sort()

        for cookie in s:

            if child == len(g): # early return, no more children
                break

            if g[child] <= cookie:  # child accepts cookie
                content += 1
                child += 1

        return content