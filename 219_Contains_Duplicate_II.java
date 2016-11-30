/*
https://leetcode.com/problems/contains-duplicate-ii/
Given an array of integers and an integer k, find out whether there are two 
distinct indices i and j in the array such that nums[i] = nums[j] 
and the difference between i and j is at most k.
** Store seen values in window, remove elements earlier than window.
Time - O(n)
Space - O(n)
 */

public class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        Set<Integer> set = new HashSet<Integer>();
        for (int i=0; i<nums.length; ++i) {
            if (!set.add(nums[i]))	// returns false if already in set
                return true;
	        if (i-k >= 0)		// remove elements outside window
                set.remove(nums[i-k]);
        }
    return false;
    }
}