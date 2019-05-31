_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/super-washing-machines/
# You have n super washing machines on a line. Initially, each washing machine has some dresses or is empty.
# For each move, you could choose any m (1 ? m ? n) washing machines, and pass one dress of each washing machine to one
# of its adjacent washing machines at the same time .
# Given an integer array representing the number of dresses in each washing machine from left to right on the line,
# you should find the minimum number of moves to make all the washing machines have the same number of dresses.
# If it is not possible to do it, return -1.

# Max of max positive balance on any machine, and max imbalance from any machine to the next (since dresses must flow
# to correct that imbalance).
# Time - O(n)
# Space - O(1)

class Solution(object):
    def findMinMoves(self, machines):
        """
        :type machines: List[int]
        :rtype: int
        """
        dresses = sum(machines)
        if dresses % len(machines) != 0:    # early return if not possible
            return -1

        target = dresses // len(machines)
        moves, running = 0, 0
        machines = [m - target for m in machines]

        for machine in machines:
            running += machine
            # max of the net imbalance for any split point and the positive balance on the current machine
            moves = max(moves, abs(running), machine)

        return moves