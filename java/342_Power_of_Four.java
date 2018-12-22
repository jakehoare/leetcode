/*
https://leetcode.com/problems/power-of-four/
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Num is positive, and a power of 2 (only one bit is set) and the bit that is set is in an even position.
Time - O(1)
Space - O(1)
*/

public class Solution {
    public boolean isPowerOfFour(int num) {
        return (num > 0) && ((num & (num - 1)) == 0) && ((num & 0x55555555) == num);
    }
}
