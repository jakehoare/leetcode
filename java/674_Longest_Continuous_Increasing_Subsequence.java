/*
https://leetcode.com/problems/longest-continuous-increasing-subsequence/
Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).

Iterate over array. If num is greater than previous, increment current length. Else update longest length and reset
current sequence.
Time - O(n)
Space - O(1)
*/

class Solution {
    public int findLengthOfLCIS(int[] nums) {

        if (nums.length == 0)
            return 0;

        int current = 1;
        int longest = 1;
        for (int i = 1; i < nums.length; ++i) {
            if (nums[i] > nums[i - 1])
                ++current;
            else {
                longest = Math.max(longest, current);
                current = 1;
            }
        }

        return Math.max(longest, current);
    }
}
