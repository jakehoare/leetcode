_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/prison-cells-after-n-days/
# There are 8 prison cells in a row, and each cell is either occupied or vacant.
# Each day, whether the cell is occupied or vacant changes according to the following rules:
# If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
# Otherwise, it becomes vacant.
# Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.
# We describe the current state of the prison in the following way: cells[i] == 1 if the i-th cell is occupied,
# else cells[i] == 0.
# Given the initial state of the prison, return the state of the prison after N days and N such changes.

# For 8 cells, the ends are vacant after the first day so there are at most 2**6 = 64 possible states.
# After at most 64 days there will be a cycle in the pattern of cells. Evolve the cells until a repeated state is
# found. Subtract as many cycles as possible from the remaining days, then evolve to the final state.
# Time - O(1)
# Space - O(1)

class Solution(object):
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        day = 0
        state = tuple(cells)                # state can be a dict key
        state_to_day = {}

        def next_state(state):
            return tuple([0] + [int(not (state[i - 1] ^ state[i + 1])) for i in range(1, 7)] + [0])

        while day < N and state not in state_to_day:    # until cycle in states
            state_to_day[state] = day
            day += 1
            state = next_state(state)

        if day < N:
            cycle = day - state_to_day[state]
            remaining = (N - state_to_day[state]) % cycle
            for _ in range(remaining):
                state = next_state(state)

        return list(state)