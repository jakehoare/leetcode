_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/number-of-digit-one/
# Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

# Calculate the number of 1s in each position, starting with units and moving forwards.
# In each position we consider the n+1 numbers from 0 to n inclusive.
# block_size is the cycle length before the pattern of 1s repeats.
# Count the number of complete blocks in n+1, each such block having 1/10th of its size of 1s.
# Then add the partial blocks.

# Time - O(log n)
# Space - O(1)

class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        ones = 0

        block_size = 10
        for _ in range(len(str(n))):

            blocks, rem = divmod(n + 1, block_size)
            ones += blocks * block_size // 10       # nb blocks * nb ones in a block
            ones += min(block_size // 10, max(0, rem - block_size // 10))   # partial blocks
            block_size *= 10

        return ones

print(Solution().countDigitOne(524))
