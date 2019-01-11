/*
https://leetcode.com/problems/logger-rate-limiter/
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Binary search the range from 1 to n inclusive.  Use long for mid to avoid overflow with mid * mid.
Return false if left and right are inverted.
Time - O(log n)
Space - O(1)
*/

public class Solution {
    public boolean isPerfectSquare(int num) {
        long left = 1;
        long right = num;

        while (left <= right) {
            long mid = left + (right - left) / 2;

            if (mid * mid == num)
                return true;
            else if (mid * mid > num)   // mid too big, sqrt(num) must be LHS of mid
                right = mid - 1;
            else
                left = mid + 1;
        }

        return false;
    }
}
