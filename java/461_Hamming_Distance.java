/*
https://leetcode.com/problems/hamming-distance/
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Given two integers x and y, calculate the Hamming distance.

Calculate x XOR y, which sets the different bits. Whilst non-zero remove last bit and increment hamming count if
that bit is set.
Time - O(n), length of max(x, y) in bits
Space - O(n)
*/

public class Solution {
    public int hammingDistance(int x, int y) {

        int distance = 0;
        int z = x ^ y;

        while (z != 0) {
            if ((z % 2) == 1)
                ++distance;
            z >>= 1;
        }
        return distance;
    }
}
