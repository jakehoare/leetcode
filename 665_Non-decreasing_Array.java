/*
https://leetcode.com/problems/non-decreasing-array/
Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.
We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

Iterate over nums whecking for increasing pairs. If amendment already made, return false. Else set amendment flag.
Prefer to reduce nums[i - 1] if this is consistent with nums[i - 2], which means nums[i] is unchanged. Else we must
increase nums[i].
Time - O(n)
Space - O(1)
*/

class Solution {
    public boolean checkPossibility(int[] nums) {

        boolean amended = false;        // flag when an amendment has already been made

        for (int i = 1; i < nums.length; ++i) {

            if (nums[i] < nums[i - 1]) {
                if (amended)
                    return false;

                amended = true;
                // decrease nums[i - 1] if possible (do not need to amend nums array)
                if (i - 1 == 0 || nums[i - 2] <= nums[i])
                    continue;

                // else increase nums[i]
                nums[i] = nums[ i - 1];
            }
        }
        return true;
    }
}