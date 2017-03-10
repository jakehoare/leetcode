/*
https://leetcode.com/problems/intersection-of-two-arrays/
Given two arrays, write a function to compute their intersection.

Convert one array to a set.  For each element in other array, if in first array set add to intersection.  Convert
intersection to array.
Time - O(m + n)
Space - O(m + n)
*/


public class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {

        Set<Integer> nums1Set = new HashSet();
        for (int n : nums1) {
            nums1Set.add(n);
        }

        Set<Integer> intersect = new HashSet();
        for (int n : nums2) {
            if (nums1Set.contains(n)) {
                intersect.add(n);
            }
        }

        int[] result = new int[intersect.size()];
        int index = 0;
        for(int i : intersect) {
            result[index++] = i;
        }
        return result;
    }
}