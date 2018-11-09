/*
https://leetcode.com/problems/power-of-two/
Given an integer, write a function to determine if it is a power of two.

Subtracting 1 from a power of 2 sets all the bits to the right of the bit that was originally set.
So no bits are set on both n and n-1.  If not a power of 2 then the higest bit set in n will also
be set in n-1.
Alternatively, count the number of bits that are set by repeatedly right=shifting.
Time - O(log n)
Space - O(1)
*/

public class Solution {
    public boolean isPowerOfTwo(int n) {
        if (n <= 0)
            return false;
        return (n & (n-1)) == 0;
    }
}
