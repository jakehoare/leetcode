/*
https://leetcode.com/problems/longest-palindrome/
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that
can be built with those letters. This is case sensitive, for example "Aa" is not considered a palindrome here.

Create a set of all chars with odd frequenceies. When a char has even frequency, remove from set and add 2 to length.
If any odd frequency remains, add 1 to length for central char.
Time - O(n)
Space - O(1)
*/

public class Solution {
    public int longestPalindrome(String s) {

        HashSet<Character> odd = new HashSet<Character>();
        int longest = 0;

        for (int i = 0; i < s.length(); ++i) {
            char c = s.charAt(i);
            if (odd.contains(c)) {
                odd.remove(c);
                longest += 2;
            }
            else
                odd.add(c);
        }

        if (!odd.isEmpty())
            ++longest;
        return longest;
    }
}
