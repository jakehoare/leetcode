/*
https://leetcode.com/problems/ransom-note/
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function
that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.
Each letter in the magazine string can only be used once in your ransom note.
You may assume that both strings contain only lowercase letters.

Count magazine letter frequencies in an array.  Decrement count for each letter in ransomNote, returning false if
any letter count is negative.
Alternatively if unknown set of characters use hashmap as counter.
Time - O(m), magazine length
Space - O(1)
*/

public class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {

        if (ransomNote.length() > magazine.length())
            return false;

        int[] counter = new int[26];

        for (int i = 0; i < magazine.length(); ++i)
            ++counter[(int) magazine.charAt(i) - (int) 'a'];

        for (int j = 0; j < ransomNote.length(); ++j) {
            if (--counter[(int) ransomNote.charAt(j) - (int) 'a'] == -1)
                return false;
        }

        return true;
    }
}
