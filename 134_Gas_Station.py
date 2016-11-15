_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/gas-station/
# There are N gas stations along a circular route, where the amount of gas at station i is gas[i].
# You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next
# station (i+1). You begin the journey with an empty tank at one of the gas stations.
# Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

# If total gas >= total cost then a circuit is possible.  There must be some journey leg that is possible, so we can
# add the net gas balance from that to the next journey leg and repeat.
# Perform a theoretical circuit and find the leg where tha gas is minimal.  Start from next station.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost):
            return -1

        tank = 0
        min_tank = float('inf')

        for station in range(len(gas)):
            tank += gas[station] - cost[station]
            if tank < min_tank:
                min_tank = tank
                min_station = station

        return (min_station+1) % len(gas)