_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/fair-candy-swap/
# Alice and Bob have candy bars of different sizes: A[i] is the size of the i-th bar of candy that Alice has,
# and B[j] is the size of the j-th bar of candy that Bob has.
# Since they are friends, they would like to exchange one candy bar each so that after the exchange,
# they both have the same total amount of candy.
# The total amount of candy a person has is the sum of the sizes of candy bars they have.
# Return an integer array ans where ans[0] is the size of the candy bar that Alice must exchange, and ans[1] is the
# size of the candy bar that Bob must exchange.
# If there are multiple answers, you may return any one of them. It is guaranteed an answer exists.

# The difference of the sizes of the bars that they must swap is half of the difference of their total candy, since
# exchanging such bars will make the difference zero. For each bar in A, check if there is bar in B with the
# required difference.
# Time - O(m + n)
# Space - O(n)

class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        A_candy, B_candy = sum(A), sum(B)
        difference = (A_candy - B_candy) // 2   # difference of sizes of bars that must be exchanged

        B_set = set(B)
        for a in A:
            if a - difference in B_set:
                return [a, a - difference]

        return []