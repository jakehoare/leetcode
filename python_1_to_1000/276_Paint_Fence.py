_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/paint-fence/
# There is a fence with n posts, each post can be painted with one of the k colors.
# You have to paint all the posts such that no more than two adjacent fence posts have the same color.
# Return the total number of ways you can paint the fence.
# n and k are non-negative integers.

# Base cases of zero or one post are 0 or k respectively. For more than 1 post, track the number of ways when the last
# 2 posts are same and when they are different. Update same as previous different, since we add the next post as the
# same colour as previous. Update different as (k - 1) * (same + different) since any previous way of either same or
# different can add a post that is not the same colour as the last post.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return k

        same, different = 0, k

        for _ in range(n - 1):
            same, different = different, (same + different) * (k - 1)

        return same + different