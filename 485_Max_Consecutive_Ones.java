/*
https://leetcode.com/problems/max-consecutive-ones/
Given a binary array, find the maximum number of consecutive 1s in this array.

Iterate over array, incrementing current consecutive count for every 1, resetting and updating max for every 0.
Time - O(n)
Space - O(1)
*/

public class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {

        int consec = 0;
        int maxConsec = 0;

        for (int num : nums) {
            if (num == 0) {
                maxConsec = Math.max(maxConsec, consec);
                consec = 0;
            } else {
                ++consec;
            }
        }
        return Math.max(maxConsec, consec);     // case of nums ending in 1s
    }
}