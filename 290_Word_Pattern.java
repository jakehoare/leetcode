/*
https://leetcode.com/problems/word-pattern/
Given a pattern and a string str, find if str follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.
You may assume both pattern and str contain only lowercase letters.

HashMap maps both chars from pattern and Strings from str to their last observed indices.
put() returns previous Integer index values, if different then char/String were previously mapped to a different pair.
Time - O(n), number of chars in str
Space - O(n)
*/

public class Solution {
    public boolean wordPattern(String pattern, String str) {

        String[] strSplit = str.split(" ");
        if (strSplit.length != pattern.length())
            return false;

        Map lastIndex = new HashMap();

        for (Integer i = 0; i < pattern.length(); ++i) {
            char c = pattern.charAt(i);
            if (lastIndex.put(c, i) != lastIndex.put(strSplit[i], i))
                return false;
        }
        return true;

    }
}