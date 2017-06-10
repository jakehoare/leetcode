/*
https://leetcode.com/problems/find-all-anagrams-in-a-string/
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
Strings consists of lowercase English letters only.

Sliding window over s of length of p, counting frequencies of all chars of s in window minus all chars in p. Also
track number of non-zero letters.
Time - O(n)
Space - O(1)
*/

public class Solution {
    public List<Integer> findAnagrams(String s, String p) {

        List<Integer> result = new LinkedList<Integer>();
        if (p.length() > s.length())
            return result;
        int[] window = new int[26];

        for (int i = 0; i < p.length(); ++i) {      // initialise window for length of p
            char c = p.charAt(i);
            --window[p.charAt(i) - 'a'];
            ++window[s.charAt(i) - 'a'];
        }

        int usedChars = 0;
        for (int i = 0; i < 26; ++i) {
            if (window[i] != 0)
                ++usedChars;
        }

        if (usedChars == 0)
            result.add(new Integer(0));

        for (int i = p.length(); i < s.length(); ++i) {
            ++window[s.charAt(i) - 'a'];
            if (window[s.charAt(i) - 'a'] == 0)
                --usedChars;
            if (window[s.charAt(i) - 'a'] == 1)
                ++usedChars;

            --window[s.charAt(i - p.length()) - 'a'];
            if (window[s.charAt(i - p.length()) - 'a'] == 0)
                --usedChars;
            if (window[s.charAt(i - p.length()) - 'a'] == -1)
                ++usedChars;

            if (usedChars == 0)
                result.add(new Integer(i - p.length() + 1));
            }

        return result;
    }
}

