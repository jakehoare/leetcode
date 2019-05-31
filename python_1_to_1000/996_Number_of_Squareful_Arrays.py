_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/number-of-squareful-arrays/
# Given an array A of non-negative integers, the array is squareful if for every pair of adjacent elements,
# their sum is a perfect square.
# Return the number of permutations of A that are squareful.
# Two permutations A1 and A2 differ if and only if there is some index i such that A1[i] != A2[i].

# Create a mapping from each number to all numbers that sum to a square.
# Start the permutation with any element. For each next element that can sum to a square, if the count of that element
# is not zero, use the element and recurse. Add the element back to the count when backtracking.
# Time - O(n**n)
# Space - O(n)

from collections import defaultdict, Counter

class Solution(object):
    def numSquarefulPerms(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        freq = Counter(A)               # counts of each element of A
        pairs = defaultdict(set)        # map element to the set of elements that sum to a square
        unique = list(freq.keys())
        pairs[None] = unique            # any element can start an empty permutation

        for i, num1 in enumerate(unique):   # create pairs mapping
            for num2 in unique[i:]:
                if int((num1 + num2) ** 0.5) ** 2 == num1 + num2:
                    pairs[num1].add(num2)
                    pairs[num2].add(num1)

        def helper(num, length):        # returns the nb permutations given previous num and permutation length

            if length == len(A):        # used all elements successfully
                return 1

            count = 0
            for next_num in pairs[num]: # for each next num that makes a square sum
                if freq[next_num] > 0:  # must have some elements remaining
                    freq[next_num] -= 1 # decrement count
                    count += helper(next_num, length + 1)
                    freq[next_num] += 1 # increment count

            return count

        return helper(None, 0)
