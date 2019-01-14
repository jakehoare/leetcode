/*
https://leetcode.com/problems/find-pivot-index/
Given an array of integers nums, write a method that returns the "pivot" index of this array.
We define the pivot index as the index where the sum of the numbers to the left of the index is equal to the sum of
the numbers to the right of the index.
If no such index exists, we should return -1.
If there are multiple pivot indexes, you should return the left-most pivot index.

Start leftSum as 0 and rightSum as sum of nums. For each num, remove from rightSum, check if left and right are equal,
add to leftSum.
Time - O(n)
Space - O(1)
*/

class Solution {
    public int pivotIndex(int[] nums) {

        int leftSum = 0;
        int rightSum = 0;
        for (int num:nums)
            rightSum += num;

        for (int i = 0; i < nums.length; ++i) {

            rightSum -= nums[i];
            if (leftSum == rightSum)
                return i;
            leftSum += nums[i];
        }

        return -1;
    }
}
