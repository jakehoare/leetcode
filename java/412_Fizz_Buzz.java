/*
https://leetcode.com/problems/fizz-buzz/
Write a program that outputs the string representation of numbers from 1 to n.
But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”.
For numbers which are multiples of both three and five output “FizzBuzz”.

Time - O(n)
Space - O(n)
*/

public class Solution {
    public List<String> fizzBuzz(int n) {

        ArrayList results = new ArrayList();

        for (int i = 1; i <= n; ++i) {
            if (i % 15 == 0)
                results.add("FizzBuzz");
            else if (i % 5 == 0)
                results.add("Buzz");
            else if (i % 3 == 0)
                results.add("Fizz");
            else
                results.add(String.valueOf(i));
        }
        return results;
    }
}
