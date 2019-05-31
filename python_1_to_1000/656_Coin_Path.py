_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/coin-path/
# Given an array A (index starts at 1) consisting of N integers: A1, A2, ..., AN and an integer B. The integer B
# denotes that from any place (suppose the index is i) in the array A, you can jump to any one of the place in the
# array A indexed i+1, i+2, …, i+B if this place can be jumped to. Also, if you step on the index i, you have to
# pay Ai coins. If Ai is -1, it means you can’t jump to the place indexed i in the array.
# Now, you start from the place indexed 1 in the array A, and your aim is to reach the place indexed N using the
# minimum coins. You need to return the path of indexes (starting from 1 to N) in the array you should take to get
# to the place indexed N using minimum coins.
# If there are multiple paths with the same cost, return the lexicographically smallest such path.
# If it's not possible to reach the place indexed N then you need to return an empty array.

# Dynamic programming. List contains the least coins to reach every index and it's path. Intialize the cost as
# infinity and empty path apart from the first index. For all reachable indices of A, update their cost with the
# the cost from i if better.
# Time - O(nB)
# Space - O(n)

class Solution(object):
    def cheapestJump(self, A, B):
        """
        :type A: List[int]
        :type B: int
        :rtype: List[int]
        """
        cheapest = [[float("inf"), []] for _ in range(len(A))]  # [cost, path] to reach each index of A
        cheapest[0] = [A[0], [1]]

        for i, cost in enumerate(A[:-1]):                       # do not jump from last index

            if cost == -1:                                      # cannot jump from i
                continue

            for j in range(i + 1, min(i + B + 1, len(A))):

                if A[j] == -1:                                  # cannot jump to j
                    continue
                new_cost = cheapest[i][0] + A[j]
                new_path = cheapest[i][1] + [j + 1]             # extend path
                cheapest[j] = min(cheapest[j], [new_cost, new_path])    # lowest cost then lowest lexicographic path

        return cheapest[-1][1]