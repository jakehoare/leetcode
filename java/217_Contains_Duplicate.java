/*
https://leetcode.com/problems/contains-duplicate/
Given an array of integers, find if the array contains any duplicates. 
Your function should return true if any value appears at least twice in the array, 
and it should return false if every element is distinct.

Store seen values in set, return true if any repeats.
Time - O(n)
Space - O(n)
 */

public class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> set = new HashSet<Integer>();
        for (int i : nums) {
            if (!set.add(i))	// returns false if already in set
                return true;
        }
    return false;
    }
}
