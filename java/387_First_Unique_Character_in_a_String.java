/*
https://leetcode.com/problems/first-unique-character-in-a-string/
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Count frequencies of each letter. Iterate over string again, return index of first letter with frequency of 1.
Time - O(n)
Space - O(1)
*/

public class Solution {
    public int firstUniqChar(String s) {

        int[] frequencies = new int[26];

        for (int i = 0; i < s.length(); ++i)
            ++frequencies[(int) s.charAt(i) - (int) 'a'];

        for (int i = 0; i < s.length(); ++i)
            if (frequencies[(int) s.charAt(i) - (int) 'a'] == 1)
                return i;
        return -1;
    }
}
