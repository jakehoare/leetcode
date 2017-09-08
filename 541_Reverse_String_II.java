/*
https://leetcode.com/problems/reverse-string-ii/
Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the
start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but
greater than or equal to k characters, then reverse the first k characters and left the other as original.

Alternately reverse and do not reverse substrings of length k.
Time - O(n)
Space - O(n)
*/

class Solution {
    public String reverseStr(String s, int k) {

        StringBuilder sb = new StringBuilder();
        int i = 0;
        boolean reverse = true;
        String sub;

        while (i < s.length()) {
            sub = s.substring(i, Math.min(i + k, s.length()));
            if (!reverse)
                sb.append(sub);
            else
                sb.append(new StringBuilder(sub).reverse());

            i += k;
            reverse = !reverse;
        }

        return sb.toString();
    }
}