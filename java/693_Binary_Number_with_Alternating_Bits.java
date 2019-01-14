/*
https://leetcode.com/problems/binary-number-with-alternating-bits/
Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have
different values.

Staring with least significant, check each digit is different from previous.
Time - O(log n)
Space - O(1)
*/

class Solution {
    public boolean hasAlternatingBits(int n) {

        int digit;
        int prev = -1;

        while (n > 0) {
            digit = n % 2;
            if (digit == prev)
                return false;
            n /= 2;
            prev = digit;
        }
        return true;
    }
}
