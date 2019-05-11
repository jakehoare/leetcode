_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/moving-stones-until-consecutive-ii/
# On an infinite number line, the position of the i-th stone is given by stones[i].
# Call a stone an endpoint stone if it has the smallest or largest position.
# Each turn, pick up an endpoint stone and move it to an unoccupied position so that it is no longer an endpoint stone.
# In particular, if the stones are at say, stones = [1,2,5], you cannot move the endpoint stone at position 5,
# since moving it to any position (such as 0, or 3) will still keep that stone as an endpoint stone.
# The game ends when you cannot make any more moves, ie. the stones are in consecutive positions.
# When the game ends, what is the minimum and maximum number of moves that you could have made?
# Return the answer as an length 2 array: answer = [minimum_moves, maximum_moves]

# The maximum moves happens when we move either the laft or right stone first then gradually fill all the gaps
# between stones, apart from the first or last gap depending on which stone moves first.
# To find the minimum gap, consider a sliding window of length n where n is the number of stones.
# Find the number of moves required to fill each window for each stone at the right end of the window.
# The number of moves is the number of stones outside the window, plus one if only the first position of the window
# is unoccupied (because we cannot move a stone to an endpoint).
# Time - O(n)
# Space - O(n)

from collections import deque

class Solution(object):
    def numMovesStonesII(self, stones):
        """
        :type stones: List[int]
        :rtype: List[int]
        """
        n = len(stones)
        stones.sort()

        sum_gaps = stones[-1] - stones[0] - n + 1       # all gaps between stones
        max_moves = sum_gaps - min(stones[1] - stones[0] - 1, stones[-1] - stones[-2] - 1)

        window = deque()                                # stones in the sliding window
        min_moves = n

        for stone in stones:
            window.append(stone)
            while stone - window[0] >= n:               # remove stones before start of window
                window.popleft()

            moves = n - len(window)                     # move all stones into window
            if moves == 1 and window[0] != stone - n + 1:   # additional move if only first position of window is empty
                moves = 2
            min_moves = min(min_moves, moves)

        return [min_moves, max_moves]
