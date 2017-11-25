_author_ = 'jake'
_project_ = 'leetcode'

# https://leetcode.com/problems/gas-station/
# There are N gas stations along a circular route, where the amount of gas at station i is gas[i].
# You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next
# station (i+1). You begin the journey with an empty tank at one of the gas stations.
# Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

# If total gas >= total cost then a circuit is possible.
# Iterate round the circuit, updating current tank balance and total. If current tank is negative, cannot start at
# that station so update start to next possible station.
# Time - O(n)
# Space - O(1)

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        start, tank, total = 0, 0, 0

        for station in range(len(gas)):
            balance = gas[station] - cost[station]
            tank += balance
            total += balance
            if tank < 0:
                start = station + 1
                tank = 0

        return -1 if total < 0 else start