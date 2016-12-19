/*
https://leetcode.com/problems/palindrome-permutation/
Given a string, determine if a permutation of the string could form a palindrome.

Add each character to a set.  If caharcter is seen twice then remove it from set.  Set contains all chars with and
odd count.  Palindrome can have at most one such char.
Time - O(n)
Space - O(n)
*/

public class Solution {
    public boolean canPermutePalindrome(String s) {

        Set<Character> charFound = new HashSet<Character>();

        for (int i = 0; i < s.length(); ++i) {

            char c = s.charAt(i);
            if (charFound.contains(c))
                charFound.remove(c);
            else
                charFound.add(c);
        }

        return charFound.size() <= 1;
    }
}