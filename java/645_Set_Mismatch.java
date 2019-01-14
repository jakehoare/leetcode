/*
https://leetcode.com/problems/set-mismatch/
The set S originally contains numbers from 1 to n. But unfortunately, due to the data error, one of the numbers in the
set got duplicated to another number in the set, which results in repetition of one number and loss of another number.
Given an array nums representing the data status of this set after the error. Your task is to firstly find the number
occurs twice and then find the number that is missing. Return them in the form of an array.

For each num, flip the sign of nums[abs(num) - 1] to indicate that num has been seen. If the sign of nums[abs(num) - 1]
is already negative, duplicate is found.
The on second iteration, find the index whose sign has not been flipped.
Time - O(n)
Space - O(1)
*/

class Solution {
    public int[] findErrorNums(int[] nums) {

        int result[] = new int[2];

        for (int num : nums) {
            if (nums[Math.abs(num) - 1] < 0)
                result[0] = Math.abs(num);
            else
                nums[Math.abs(num) - 1] *= -1;
        }

        for (int i = 0; i < nums.length; ++i) {
            if (nums[i] > 0) {
                result[1] = i + 1;
                break;
            }
        }

        return result;
    }
}
