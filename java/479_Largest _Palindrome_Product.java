/*
https://leetcode.com/problems/largest-palindrome-product/
Find the largest palindrome made from the product of two n-digit numbers.
Since the result could be very large, you should return the largest palindrome mod 1337.

For a given n find the largest possible number which is a product. Take the first half of the digits of this
number and reverse them to create the largest possible palindrome. Test if this palindrome is a product by checking
factors with n digits starting from 10**n - 1 and stopping at sqrt(palindrome). If not, decrement the first half.
Time - O(10**2n), 10**n firstHalf to check, each of which is checked for 10**n factors
Space - O(n)
*/

public class Solution {
    public int largestPalindrome(int n) {

        if(n == 1)
            return 9;

        int upperBound = (int) Math.pow(10, n) - 1;     // factors must be <= upperBound
        int lowerBound = (upperBound / 10);             // factors must be > lowerBound
        long maxNumber = (long) upperBound * (long) upperBound;     // max possible palindrome

        // first half of the maximum possible palindrome
        int firstHalf = (int) (maxNumber / (long) Math.pow(10, n));

        boolean palindromeFound = false;
        long palindrome = 0;

        while (!palindromeFound) {
            // create maximum possible palindrome
            palindrome = createPalindrome(firstHalf);

            // try all possible factors i and palindrome/i
            for (long i = upperBound; upperBound > lowerBound; i--) {
                // stop if largest factor squared cannot make palindrome
                if (i * i < palindrome)
                    break;

                // two factors found, both are n-digits
                if (palindrome % i == 0) {
                    palindromeFound = true;
                    break;
                }
            }

            firstHalf--;
        }
        return (int) (palindrome % 1337);
    }

    private long createPalindrome(long num) {
        String str = num + new StringBuilder().append(num).reverse().toString();
        return Long.parseLong(str);
    }
}
