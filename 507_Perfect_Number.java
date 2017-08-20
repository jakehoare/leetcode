/*
https://leetcode.com/problems/perfect-number/
We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.
Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.

Try all divisors from 2 to sqrt(n).
Time - O(sqrt(n))
Space - O(1)
*/

class Solution {
    public boolean checkPerfectNumber(int num) {

        if (num == 1)       // no divisors apart from self
            return false;

        int sumDivisors = 1;
        int maxDivisor = (int) Math.sqrt(num);
        for (int i = 2; i <= maxDivisor; ++i) {
            if (num % i == 0)
                sumDivisors += i + num/i;
        }

        if (maxDivisor * maxDivisor == num)     // double-counted if num is a square
            sumDivisors -= maxDivisor;

        return sumDivisors == num;
    }
}