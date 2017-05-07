/*
https://leetcode.com/problems/nth-digit/
Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

Find the length of the number containing the nth digit by removing 9 digits of length 1, 90 of length 2, etc.
Find the integer containing n by dividing remainder by its length and adding the starting integer of that length.
Time - O(log n)
Space - O(1)
*/

public class Solution {
	public int findNthDigit(int n) {
	    n--;
		int length = 1;
		long count = 9;

		while (n >= length * count) {
			n -= length * count;
			length += 1;
			count *= 10;
		}

        int intOfN = (n / length) + (int) Math.pow(10, length - 1);
		String s = Integer.toString(intOfN);
		return (int) (s.charAt(n % length)) - '0';
	}
}