/*
https://leetcode.com/problems/reverse-string/
Write a function that takes a string as input and returns the string reversed.

Use built-in StringBuilder.
Time - O(n)
Space - O(n)
*/


public class Solution {
    public String reverseString(String s) {
        return new StringBuilder(s).reverse().toString();
    }
}