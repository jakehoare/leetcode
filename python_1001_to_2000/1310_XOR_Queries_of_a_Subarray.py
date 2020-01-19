_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/xor-queries-of-a-subarray/
# Given the array arr of positive integers and the array queries where queries[i] = [Li, Ri],
# for each query i compute the XOR of elements from Li to Ri (that is, arr[Li] xor arr[Li+1] xor ... xor arr[Ri] ).
# Return an array containing the result for the given queries.

# Calculate cumulative XOR up to each element.
# For each query, take the difference between cumulative XOR of start and end + 1 indices.
# Time - O(m + n) for m queries and arr of length n
# Space - O(m + n)

class Solution(object):
    def xorQueries(self, arr, queries):
        """
        :type arr: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        xor = [0]
        for num in arr:
            xor.append(xor[-1] ^ num)

        result = []
        for start, end in queries:
            result.append(xor[end + 1] ^ xor[start])

        return result
