/*
https://leetcode.com/problems/min-cost-climbing-stairs/
On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).
Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the
floor, and you can either start from the step with index 0, or the step with index 1.

Iterate backwards. Cost from any step is the cost of using that step plus the minimum cost from next two steps.
Time - O(n)
Space - O(1)
*/

class Solution {
    public int minCostClimbingStairs(int[] cost) {
        
        for (int i = cost.length - 3; i >= 0; --i)
            cost[i] += Math.min(cost[i + 1], cost[i + 2]);

        return Math.min(cost[0], cost[1]);      // start at either of the first 2 steps
    }
}