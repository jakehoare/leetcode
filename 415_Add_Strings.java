/*
https://leetcode.com/problems/third-maximum-number/
Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return
the maximum number.

Iterate over stings from end to front or carry. If either sting has ended, use zero. Add digits plus carry and mod 10.
Reverse result.
Time - O(n)
Space - O(n)
*/

public class Solution {
    public String addStrings(String num1, String num2) {

        StringBuilder result = new StringBuilder();
        int carry = 0;
        for(int i = num1.length() - 1, j = num2.length() - 1; i >= 0 || j >= 0 || carry == 1; i--, j--) {
            int x = i < 0 ? 0 : num1.charAt(i) - '0';
            int y = j < 0 ? 0 : num2.charAt(j) - '0';
            result.append((x + y + carry) % 10);
            carry = (x + y + carry) / 10;
        }
        return result.reverse().toString();
    }
}