/*
https://leetcode.com/problems/valid-word-abbreviation/
Given a non-empty string s and an abbreviation abbr, return whether the string matches with the given abbreviation.

Use pointers to the next char to be checked in word and abbr. If matching letters, move pointers on. If abbr is a char
(does not macth word) return false. Else parse integer in abbr and move forward pointer in word by the integer.
Return true if both pointers are at ends.
Time - O(n)
Space - O(1)
*/

public class Solution {
    public boolean validWordAbbreviation(String word, String abbr) {

        int i = 0;
        int j = 0;

        while (i < abbr.length() && j < word.length()) {

            char c = abbr.charAt(i);
            if (c == word.charAt(j)) {
                ++i;
                ++j;
                continue;
            }

            if (!Character.isDigit(c) || c == '0')  // digit cannot have leading zero
                return false;

            int num = 0;
            while (i < abbr.length() && Character.isDigit(abbr.charAt(i))) {
                num = num * 10 + Character.getNumericValue(abbr.charAt(i));
                ++i;
            }
            j += num;
        }

        return (i == abbr.length() && j == word.length());
    }
}