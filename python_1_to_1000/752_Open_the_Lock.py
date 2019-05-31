_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/open-the-lock/
# You have a lock in front of you with 4 circular wheels.
# Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'.
# The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'.
# Each move consists of turning one wheel one slot.
# The lock initially starts at '0000', a string representing the state of the 4 wheels.
# You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock
# will stop turning and you will be unable to open it.
# Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of
# turns required to open the lock, or -1 if it is impossible.

# Bidirectional breadth-first search. From the starting position, move one wheel to all next positions. Expand frontier
# until target is found, ignoring deadends and already seen combinations. Swap queue with target after every iteration
# to limit the size of the frontier.
# Time - O(1), limit of 10000 possible combinations
# Space - O(1)

class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        queue, target = {"0000"}, {target}
        visited = set()
        deadends = set(deadends)
        steps = 0

        def shift(combo):   # find all combinations that can be reached by moving one wheel
            shifts = set()
            for i, c in enumerate(combo):       # for each wheel
                shifted = (int(c) + 1) % 10     # move up
                shifts.add(combo[:i] + str(shifted) + combo[i + 1:])
                shifted = (int(c) - 1) % 10     # move down
                shifts.add(combo[:i] + str(shifted) + combo[i + 1:])
            return shifts

        while queue:

            if target & queue:      # intersection between queue and target
                return steps

            new_queue = set()
            steps += 1

            for combo in queue:

                if combo in visited or combo in deadends:
                    continue        # ignore combinations seen before or not allowed
                visited.add(combo)
                new_queue |= shift(combo)       # add all shifted combinations

            queue, target = target, new_queue   # update queue and swap queue with target

        return -1
