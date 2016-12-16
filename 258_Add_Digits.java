/*
https://leetcode.com/problems/add-digits/
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Digital root.  Alternative closed form expression is (n-1)%9 + 1.
Time - O(log n)
Space - O(1)
*/

public class Solution {
    public int addDigits(int num) {

        while (num > 9) {           // more than one digit

            int digitSum = 0;
            while (num > 0) {       // sum all digits
                digitSum += num % 10;
                num /= 10;
            }
            num = digitSum;

        }
        return num;
    }
}