_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/minimum-time-to-build-blocks/
# You are given a list of blocks, where blocks[i] = t means that the i-th block needs t units of time to be built.
# A block can only be built by exactly one worker.
# A worker can either split into two workers (number of workers increases by one) or build a block then go home.
# Both decisions cost some time.
# The time cost of spliting one worker into two workers is given as an integer split.
# Note that if two workers split at the same time, they split in parallel so the cost would be split.
# Output the minimum time needed to build all blocks.
# Initially, there is only one worker.

# Create a heap of the time to mine each block.
# Repeatedly pop off the smallest 2 blocks and combine them into a single block.
# Add the combined block back to the heap, with its time of split + max time to mine underlying blocks.
# Continue until only one block remains.
# Time - O(n log n)
# Space - O(n)

import heapq

class Solution(object):
    def minBuildTime(self, blocks, split):
        """
        :type blocks: List[int]
        :type split: int
        :rtype: int
        """
        heapq.heapify(blocks)

        while len(blocks) > 1:          # combine the smallest 2 blocks
            heapq.heappop(blocks)
            heapq.heappush(blocks, split + heapq.heappop(blocks))

        return blocks[0]
