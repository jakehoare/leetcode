/*
https://leetcode.com/problems/1-bit-and-2-bit-characters/
We have two special characters. The first character can be represented by one bit 0. The second character can be
represented by two bits (10 or 11).
Now given a string represented by several bits. Return whether the last character must be a one-bit character or not.
The given string will always end with a zero.

If next char is 1 then move forward 2 steps else move forward one step.
Time - O(n)
Space - O(1)
*/

class Solution {
    public boolean isOneBitCharacter(int[] bits) {

        int i = 0;

        while (i < bits.length - 1) {

            if (bits[i] == 1)
                ++i;
            ++i;
        }

        return i == bits.length - 1;    // true if final bit is visited
    }
}