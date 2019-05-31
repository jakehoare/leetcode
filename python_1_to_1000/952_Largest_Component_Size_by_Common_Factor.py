_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/largest-component-size-by-common-factor/
# Given a non-empty array of unique positive integers A, consider the following graph:
# There are A.length nodes, labelled A[0] to A[A.length - 1];
# There is an edge between A[i] and A[j] if and only if A[i] and A[j] share a common factor greater than 1.
# Return the size of the largest connected component in the graph.

# Union-find to connect the indices of elements of A with common prime factors.
# For each element of A, find the set of prime factors. For each prime factor, if not seen before then map the factor
# to the index in A of the element. Else union the index of the element with the index already mapped to the factor
# and update the size of the connected component.
# Time - O(n k**0.5 log*(n k**0.5)) since there are O(k**0.5) factors for each element
# Space - O(n)

class Solution(object):
    def largestComponentSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        def prime_factors(x):   # calculate set of prime factors of x
            factors = set()

            while x % 2 == 0:   # remove factors of 2, so next loop uses step of 2
                factors.add(2)
                x //= 2

            for i in range(3, int(x ** 0.5) + 1, 2):
                while x % i == 0:
                    factors.add(i)
                    x //= i

            if x > 2:           # x is originally prime
                factors.add(x)

            return factors

        def find(x):            # return ultimate parent of x and collapse tree
            while x != parents[x]:
                parents[x] = parents[parents[x]]    # link x to grandparent
                x = parents[x]
            return x

        def union(x, y):
            x, y = find(x), find(y)
            if x == y:
                return
            parents[x] = y      # all children of x are moved to y
            sizes[y] += sizes[x]
            sizes[x] = 0

        n = len(A)
        parents = [i for i in range(n)] # index to parent mapping
        sizes = [1] * n                 # sizes[i] is the size of component with A[i] parent
        prime_to_index = {}             # prime factor mapped to index in A of first num to use that factor

        for i, a in enumerate(A):

            primes = prime_factors(a)

            for p in primes:
                if p in prime_to_index:
                    union(i, prime_to_index[p])
                prime_to_index[p] = i

        return max(sizes)