/*
https://leetcode.com/problems/reverse-words-in-a-string-iii/
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving
whitespace and initial word order.  In the string, each word is separated by single space and there will not be
any extra space in the string.

Convert to char array. Track start of word. When end found, reverse.
Time - O(n)
Space - O(n)
*/

class Solution {
    public String reverseWords(String s) {

        char[] str = s.toCharArray();
        int start = 0;

        for (int end = 0; end < s.length(); ++end) {
            if (str[end] == ' ') {
                reverseSubarray(str, start, end - 1);
                start = end + 1;    // keep space in place and start new word
            }
        }
        reverseSubarray(str, start, s.length() - 1);    // final word
        return String.valueOf(str);
    }

    private void reverseSubarray(char[] array, int left, int right) {
        while (left < right) {
            char temp = array[left];
            array[left] = array[right];
            array[right] = temp;
            ++left;
            --right;
        }
    }
}