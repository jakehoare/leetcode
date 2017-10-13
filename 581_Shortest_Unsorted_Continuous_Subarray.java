/*
https://leetcode.com/problems/shortest-unsorted-continuous-subarray/
Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending
order, then the whole array will be sorted in ascending order, too.
You need to find the shortest such subarray and output its length.

Iterate forwards along array, always updating numsMax and updating right when nums[i] < numsMax. All nums to the right
of right are non-descending and greater than min so do not need to be sorted. Similarly iterate backwards updating
numsMin and left.
Time - O(n)
Space - O(1)
*/

class Solution {
    public int findUnsortedSubarray(int[] nums) {
        
        int numsMax = nums[0];      // nums.length guaranteed to be non-zero
        int numsMin = nums[nums.length - 1];
        int left = -1;              // initialise right and left so if not updated (sorted ascending)
        int right = -2;             // then right - left + 1 = 0

        for (int i = 1; i < nums.length; ++i) {

            numsMax = Math.max(numsMax, nums[i]);
            numsMin = Math.min(numsMin, nums[nums.length - 1 - i]);

            if (nums[i] < numsMax)
                right = i;
            if (nums[nums.length - 1 - i] > numsMin)
                left = nums.length - 1 - i;
        }

        return right - left + 1;
    }
}
