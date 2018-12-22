/*
https://leetcode.com/problems/sum-of-two-integers/
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Sum without carry is a XOR b.  Carry is when same bit is set in a AND b, shifted left.  Repeat until no carry.
Time - O(1), since 32 bits
Space - O(1)
*/

public class Solution {
    public int getSum(int a, int b) {
        while (b != 0) {
            int sum = a ^ b;
            int carry = (a & b) << 1;
            a = sum;
            b = carry;
        }
        return a;
    }
}
