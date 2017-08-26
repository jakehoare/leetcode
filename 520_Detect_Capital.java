/*
https://leetcode.com/problems/detect-capital/
Given a word, you need to judge whether the usage of capitals in it is right or not.
We define the usage of capitals in a word to be right when one of the following cases holds:
All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital if it has more than one letter, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.

All chars after second must be same case as second. First cannot be lower case and second upper case.
Time - O(n)
Space - O(1)
*/

class Solution {
    public boolean detectCapitalUse(String word) {

        if (word.length() < 2)
            return true;
        char c;

        boolean first = Character.isUpperCase(word.charAt(0));
        boolean second = Character.isUpperCase(word.charAt(1));
        if (second && !first)
            return false;

        for (int i = 2; i < word.length(); ++i) {
            c = word.charAt(i);
            if (Character.isUpperCase(c) != second)
                return false;
        }

        return true;
    }
}