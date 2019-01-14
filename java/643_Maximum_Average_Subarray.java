/*
https://leetcode.com/problems/maximum-average-subarray-i/
Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average
value. And you need to output the maximum average value.

Maintain a sliding window of length k. Iterate over end indices of window, adding a new num and dropping a num from the
start of the window.
Time - O(n)
Space - O(1)
*/

class Solution {
    public double findMaxAverage(int[] nums, int k) {

        int sum = 0;
        for (int i = 0; i < k; ++i)
            sum += nums[i];
        int maxSum = sum;

        for (int i = k; i < nums.length; ++i) {
            sum += (nums[i] - nums[i - k]);
            maxSum = Math.max(maxSum, sum);
        }

        return (double) maxSum / k;
    }
}
