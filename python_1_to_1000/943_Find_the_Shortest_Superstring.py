_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/find-the-shortest-superstring/
# Given an array A of strings, find any smallest string that contains each string in A as a substring.
# We may assume that no string in A is substring of another string in A.

# For each pair of words (in both orders) find the overlap.
# For each of the 2**n sets of words, for each word in the set as the last word used in the resulting string,
# find the most total overlap with any other word in the set as the previous word in the string.
# Time - O(n**2 (2**n + k)) where k is max string length
# Space - O(n (2**n + k)) where the nk is for the final result

class Solution:
    def shortestSuperstring(self, A):
        """
        :type A: List[str]
        :rtype: str
        """
        N = len(A)

        overlaps = [[0] * N for _ in range(N)]  # overlaps[i][j] is nb chars overlapping between x and y

        for i, x in enumerate(A):
            for j, y in enumerate(A):
                if i != j:
                    for ans in range(min(len(x), len(y)), 0, -1):
                        if x.endswith(y[:ans]):
                            overlaps[i][j] = ans
                            break

        dp = [[0] * N for _ in range(1 << N)]  # dp[mask][i] is most overlap with mask, ending with ith element
        parent = [[None] * N for _ in range(1 << N)]  # parent[mask][i] is word index of previous word

        for mask in range(1, 1 << N):  # mask has a set bit for each used word index
            for bit in range(N):

                if (mask >> bit) & 1:  # for each word used in mask

                    prev_mask = mask ^ (1 << bit)  # get mask without this word
                    if prev_mask == 0:
                        continue

                    for i in range(N):

                        if (prev_mask >> i) & 1:  # for each word in previous mask

                            overlap = dp[prev_mask][i] + overlaps[i][bit]
                            if overlap > dp[mask][bit]:  # better overlap
                                dp[mask][bit] = overlap
                                parent[mask][bit] = i

        mask = (1 << N) - 1
        i = max(range(N), key=lambda x: dp[-1][x])  # index of last word used
        result = [A[i]]
        used = {i}

        while True:

            mask, j = mask ^ (1 << i), parent[mask][i]  # get parent word and update mask
            if j is None:
                break
            overlap = overlaps[j][i]
            prefix = A[j] if overlap == 0 else A[j][:-overlap]
            result.append(prefix)
            used.add(j)
            i = j

        result = result[::-1] + [A[i] for i in range(N) if i not in used]  # reverse, add unused words

        return "".join(result)
