/*
https://leetcode.com/problems/range-sum-query-immutable/
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.
You may assume that the array does not change.  There are many calls to sumRange function.

Store the cumulative sum up to each index.  sumRange is the difference of the cumulative sums to j and to i-1.
Time - O(n) to initialise, O(1) for prefixSums()
Space - O(n)
*/

public class NumArray {

    private int[] prefixSums;

    public NumArray(int[] nums) {
        prefixSums = new int[nums.length + 1];  // prefixSums[i+1] is cumulative sum including nums[i]
        for (int i = 0; i < nums.length; ++i)
            prefixSums[i+1] = nums[i] + prefixSums[i];
    }

    public int sumRange(int i, int j) {
        return prefixSums[j+1] - prefixSums[i];
    }
}
