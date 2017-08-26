/*
https://leetcode.com/problems/longest-uncommon-subsequence-i/
Given a group of two strings, you need to find the longest uncommon subsequence of this group of two strings. The
longest uncommon subsequence is defined as the longest subsequence of one of these strings and this subsequence should
not be any subsequence of the other strings.
A subsequence is a sequence that can be derived from one sequence by deleting some characters without changing the
order of the remaining elements. Trivially, any string is a subsequence of itself and an empty string is a subsequence
of any string.
The input will be two strings, and the output needs to be the length of the longest uncommon subsequence. If the
longest uncommon subsequence doesn't exist, return -1.

If strings are not same then the longer can creaet a subsequence that is not common to shorter.
Else there is no subsequnce.
Time - O(min(m, n))
Space - O(1)
*/

class Solution {
    public int findLUSlength(String a, String b) {
        if (a.equals(b))
            return -1;
        return Math.max(a.length(), b.length());

    }
}