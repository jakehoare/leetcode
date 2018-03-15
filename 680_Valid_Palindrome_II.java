/*
https://leetcode.com/problems/valid-palindrome-ii/
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Set left and right indices to the ends of s. Iterate inwards. If characters do not match, either left or right must be
deleted so continue searching for a palindrome with no more deletions allowed.
Time - O(n)
Space - O(1)
*/

class Solution {
    public boolean validPalindrome(String s) {
        return helper(s, 0, s.length() - 1, false);
    }

    // deleted flags if a char has already been deleted
    private boolean helper(String s, int left, int right, boolean deleted) {

        while (left < right) {
            if (s.charAt(left) != s.charAt(right)) {
                if (deleted)        // already deleted a char
                    return false;
                return (helper(s, left, right - 1, true) || helper(s, left + 1, right, true)) ;
            }
            ++left;
            --right;
        }

        return true;
    }

}