/*
https://leetcode.com/problems/move-zeroes/
Given an array nums, write a function to move all 0's to the end of it while maintaining
the relative order of the non-zero elements.

Move non-zeros to front.  For each non-zero, swap with the next index after the existing block of non-zeros.
Time - O(n)
Space - O(1)
*/

public class Solution {
    public void moveZeroes(int[] nums) {

        int nextNonZero = 0;

        for (int i = 0; i < nums.length; ++i) {
            if (nums[i] != 0) {
                int temp = nums[i];
                nums[i] = nums[nextNonZero];
                nums[nextNonZero] = temp;
                ++nextNonZero;
            }
        }
    }
}