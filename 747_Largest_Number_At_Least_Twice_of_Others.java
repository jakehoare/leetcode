/*
https://leetcode.com/problems/largest-number-at-least-twice-of-others/
In a given integer array nums, there is always exactly one largest element.
Find whether the largest element in the array is at least twice as much as every other number in the array.
If it is, return the index of the largest element, otherwise return -1.

Iterate over array to find max numder and its index. Iterate again, checking each number that is not the max is not
more than half the max.
Time - O(n)
Space - O(1)
*/

class Solution {
    public int dominantIndex(int[] nums) {

        int max = -1;
        int max_i = -1;
        for (int i = 0; i < nums.length; ++i) {
            if (nums[i] > max) {
                max = nums[i];
                max_i = i;
            }
        }

        for (int num : nums)
            if (num != max && 2 * num > max)
                return -1;

        return max_i;
    }
}