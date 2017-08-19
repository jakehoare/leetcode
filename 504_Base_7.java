/*
https://leetcode.com/problems//base-7/
Given an integer, return its base 7 string representation.

Flag if negative. Repeatedly divied by 7 until zero, adding digits to StringBuilder.
Add minus sign if needed and reverse result.
Time - O(log n)
Space - O(log n)
*/

class Solution {
    public String convertToBase7(int num) {

        boolean negative = false;
        if (num < 0)
            negative = true;
        else if (num == 0)
            return "0";

        StringBuilder sb = new StringBuilder();
        while (num != 0) {
            sb.append(num % 7);
            num /= 7;
        }

        if (negative)
            sb.append('-');
        return sb.reverse().toString();
    }
}