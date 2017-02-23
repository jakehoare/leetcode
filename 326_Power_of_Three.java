/*
https://leetcode.com/problems/power-of-three/
Given an integer, write a function to determine if it is a power of three.

Find the largest power of 3 less than MAXINT.  If there is no remainder when this number is divided by n then n only
containse factors of 3.
Time - O(1)
Space - O(1)
*/

public class Solution {
    public boolean isPowerOfThree(int n) {

        double maxFactors = Math.log(Integer.MAX_VALUE) / Math.log(3);
        int maxPower = (int) Math.pow(3, (int) maxFactors);
        return (n > 0 && maxPower % n == 0);
    }
}