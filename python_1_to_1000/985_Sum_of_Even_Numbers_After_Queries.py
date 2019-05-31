_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/sum-of-even-numbers-after-queries/
# We have an array A of integers, and an array queries of queries.
# For the i-th query val = queries[i][0], index = queries[i][1], we add val to A[index].
# Then, the answer to the i-th query is the sum of the even values of A.
# Here, the given index = queries[i][1] is a 0-based index, and each query permanently modifies the array A.
# Return the answer to all queries.  Your answer array should have answer[i] as the answer to the i-th query.

# Calculate the initial sum of even values. For each query, if the value to be adjusted is even, decrement the
# even sum by this amount. Adjust the value, then if the new value is even, increment the even sum by the value.
# Time - O(n)
# Space - O(n)

class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        sum_even = sum(x for x in A if x % 2 == 0)
        result = []

        for val, i in queries:

            if A[i] % 2 == 0:
                sum_even -= A[i]
            A[i] += val
            if A[i] % 2 == 0:
                sum_even += A[i]

            result.append(sum_even)

        return result
