/*
https://leetcode.com/problems/arranging-coins/
You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.
Given n, find the total number of full staircase rows that can be formed.

Number of coins in k steps = f(k) = 1 + 2 + 3 + ... + k = k * (k + 1) / 2. Find largest k s.t. f(k) <= n.
Solve k*k + k - 2n <= 0.
Time - O(1)
Space - O(1)
*/

public class Solution {
    public int arrangeCoins(int n) {
        return (int) ((Math.sqrt(1 + 8.0 * n) - 1) / 2);
}
