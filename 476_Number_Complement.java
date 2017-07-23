/*
https://leetcode.com/problems/number-complement/
Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.
The given integer is guaranteed to fit within the range of a 32-bit signed integer.
You could assume no leading zero bit in the integer’s binary representation.

highestOneBit(num) is the number with only the highest bit of num set. Subtract 1 to set all lower bits. This creates a
mask. AND of mask with ~num sets all bits that were not set in num.
Time - O(log n)
Space - O(1)
*/

public class Solution {
    public int findComplement(int num) {

        return ~num & (Integer.highestOneBit(num) - 1);

    }
}
