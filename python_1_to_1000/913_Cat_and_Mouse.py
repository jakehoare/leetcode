_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/cat-and-mouse/
# A game on an undirected graph is played by two players, Mouse and Cat, who alternate turns.
# The graph is given as follows: graph[a] is a list of all nodes b such that ab is an edge of the graph.
# Mouse starts at node 1 and goes first, Cat starts at node 2 and goes second, and there is a Hole at node 0.
# During each player's turn, they must travel along one edge of the graph that meets where they are.
# For example, if the Mouse is at node 1, it must travel to any node in graph[1].
# Additionally, it is not allowed for the Cat to travel to the Hole (node 0.)
# Then, the game can end in 3 ways:
# If ever the Cat occupies the same node as the Mouse, the Cat wins.
# If ever the Mouse reaches the Hole, the Mouse wins.
# If ever a position is repeated (ie. the players are in the same position as a previous turn, and it is the
# same player's turn to move), the game is a draw.
# Given a graph, and assuming both players play optimally, return 1 if the game is won by Mouse, 2 if the game
# is won by Cat, and 0 if the game is a draw.

# Create a graphs of states of (mouse_node, cat_node, next_mover). Attempt to find the winner from each state.
# Initially states with mouse at node 0 has mouse as winner and states with cat at node of mouse have cat as winner.
# All other states are drawn initially. Add states with known winners to a queue.
# Initialise a count of the number of nodes that are connected to each state and do not have known winners.
# For each state in the queue, check each predecessor state with an unknown winner. If we can move from the predecessor
# to the state with the known winner, predecessor state has the same winner. Else reduce the count of unknown winners
# linked to the predecessor. If the count is zero, the animal whose turn it is to move at the predecessor cannot win.
# Time - O(n**3) since there are O(n**2) states each with O(n) links.
# Space - O(n**2)

from collections import defaultdict, deque

class Solution(object):
    def catMouseGame(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        DRAW, MOUSE, CAT = 0, 1, 2
        n = len(graph)

        def parents(mouse, cat, turn):      # find predecessor states
            if turn == CAT:
                return [(new_mouse, cat, 3 - turn) for new_mouse in graph[mouse]]
            return [(mouse, new_cat, 3 - turn) for new_cat in graph[cat] if new_cat != 0]

        state_winner = defaultdict(int)     # map from state to its winner, DRAW by default

        degree = {}                         # map node to count of connected states that are not winners
        for mouse in range(n):
            for cat in range(n):
                degree[mouse, cat, MOUSE] = len(graph[mouse])
                degree[mouse, cat, CAT] = len(graph[cat]) - (0 in graph[cat])

        queue = deque()                     # queue contains all states with known winner
        for i in range(n):
            for turn in [MOUSE, CAT]:
                state_winner[0, i, turn] = MOUSE    # mouse wins if at hole for any turn and any cat position
                queue.append((0, i, turn, MOUSE))
                if i > 0:                   # cat wins if at mouse unless at hole, for any turn and any mouse position
                    state_winner[i, i, turn] = CAT
                    queue.append((i, i, turn, CAT))

        while queue:

            i, j, turn, winner = queue.popleft()    # get state with known winner

            for i2, j2, prev_turn in parents(i, j, turn):   # for all predecessor states without known winners
                if state_winner[i2, j2, prev_turn] is DRAW:

                    if prev_turn == winner:         # can move to a winning state
                        state_winner[i2, j2, prev_turn] = winner
                        queue.append((i2, j2, prev_turn, winner))

                    else:                           # reduce count of unknown winner predecessor states
                        degree[i2, j2, prev_turn] -= 1
                        if degree[i2, j2, prev_turn] == 0:  # predecessor always leads to loss
                            state_winner[i2, j2, prev_turn] = turn
                            queue.append((i2, j2, prev_turn, turn))

        return state_winner[1, 2, MOUSE]