/*
https://leetcode.com/problems/convert-a-number-to-hexadecimal/
Given an integer, write an algorithm to convert it to hexadecimal. For negative integer, two’s complement method is used.
All letters in hexadecimal (a-f) must be in lowercase.
The hexadecimal string must not contain extra leading 0s. If the number is zero, it is represented by a single zero
character '0'; otherwise, the first character in the hexadecimal string will not be the zero character.
The given number is guaranteed to fit within the range of a 32-bit signed integer.

Extract the rightmost 4 bits and convert to letter if > 9 else keep as integer. Unsigned right shift 4 places.
Reverse result.
Time - O(n)
Space - O(n)
*/

public class Solution {
    public String toHex(int num) {

        if (num == 0)
            return "0";

        StringBuilder hex = new StringBuilder();
        while (num != 0) {

            int digit = num & 15;       // extract last 4 bits
            if (digit < 10)
                hex.append(digit);
            else
                hex.append((char) (digit - 10 + 'a'));
            num = num >>> 4;            // unsigned right shift
        }

        return hex.reverse().toString();
    }
}
