_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/network-delay-time/
# There are N network nodes, labelled 1 to N.
# Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, v is the
# target node, and w is the time it takes for a signal to travel from source to target.
# Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal?
# If it is impossible, return -1.

# Initialise the best time to reach each node as infinity apart from 0 for node K. Create a set of all nodes, find the
# node in the set with the smallest time to reach and remove it from the set, since this time cannot be improved by
# going via another node with a greater time to reach. Update the times to reach all neighbours. Repeat removing
# closest node until all nodes have been tested or closest node cannot bee reached by other nodes.
# Time - O(n**2 + e) where n is nb nodes and e is nb edges
# Space - O(n + e)

class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        best_times = [float("inf") for _ in range(N + 1)]   # best time for signal to reach any node
        best_times[K] = 0

        network = [[] for _ in range(N + 1)]                # map nodes to list of (nbor, time)
        for u, v, w in times:
            network[u].append((v, w))

        nodes = {n for n in range(1, N + 1)}                # set of all nodes to be tested

        while nodes:

            best_time = float("inf")
            for node in nodes:                              # find the remaining node with smallest time
                if best_times[node] < best_time:
                    best_time = best_times[node]
                    next_node = node

            if best_time == float("inf"):                   # best_node has not been reached
                return -1
            nodes.remove(next_node)                         # cannot improve time to reach this node

            for nbor, time in network[next_node]:           # update times to reach neighbours
                best_times[nbor] = min(best_times[nbor], best_time + time)

        return max(best_times[1:])                          # ignore best_times[0]