_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/beautiful-arrangement/
# Suppose you have N integers from 1 to N. We define a beautiful arrangement as an array that is constructed by these
# N numbers successfully if one of the following is true for the ith position (1 <= i <= N) in this array:
#   The number at the ith position is divisible by i.
#   i is divisible by the number at the ith position.
# Given N, how many beautiful arrangements can you construct?

# For each position from final index working forwards, insert all valid numbers and recurse. Backwards ensures less
# branching resulting in failures.
# Time - O(n!)
# Space - O(n)

class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        used = [False for _ in range(N + 1)]
        self.count = 0

        def helper(i):          # i is position to be filled
            if i == 0:          # solution found
                self.count += 1
                return

            for num in range(1, N + 1):
                if not used[num] and (num % i == 0 or i % num == 0):
                    used[num] = True
                    helper(i - 1)
                    used[num] = False

        helper(N)
        return self.count