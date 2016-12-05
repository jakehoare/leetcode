/*
https://leetcode.com/problems/valid-anagram/
Given two strings s and t, write a function to determine if t is an anagram of s.

In an array count the frequency of each char in the first string.  For each char in the second string decrement
the count.  At least one char count must be negative if the strings are not anagrams.
Time - O(n)
Space - O(1)
*/

public class Solution {
    public boolean isAnagram(String s, String t) {

        if (s.length() != t.length())   // early return
            return false;

        int[] letterCounts = new int[26];

        for (int i = 0; i < s.length(); ++i) {
            char c = s.charAt(i);
            letterCounts[(int) c - (int) 'a']++;
        }

        for (int i = 0; i < t.length(); ++i) {
            char c = t.charAt(i);
            letterCounts[(int) c - (int) 'a']--;
            if (letterCounts[(int) c - (int) 'a'] < 0)
                return false;
        }
        return true;
    }
}