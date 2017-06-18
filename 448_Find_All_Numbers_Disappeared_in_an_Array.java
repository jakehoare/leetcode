/*
https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
Find all the elements of [1, n] inclusive that do not appear in this array.


Time - O(n)
Space - O(1)
*/

public class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        for (int num : nums) {
            int i = Math.abs(num) - 1;      // num may have already have sign flipped so take absolute value
            if (nums[i] > 0)
                nums[i] = -nums[i];
        }

        List<Integer> missing = new LinkedList<Integer>();
        for (int i = 0; i < nums.length; ++i)
            if (nums[i] > 0)
                missing.add(i + 1);

        return missing;
    }
}