/*
https://leetcode.com/problems/array-partition-i/
Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2),
..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

Sort and sum even index nums.
Time - O(n log n)
Space - O(1)
*/

class Solution {
    public int arrayPairSum(int[] nums) {
        Arrays.sort(nums);
        int result = 0;
        for (int i = 0; i < nums.length; i += 2) {
            result += nums[i];
        }
        return result;
    }
}
