/*
https://leetcode.com/problems/repeated-string-match/
Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it.
If no such solution, return -1.
For example, with A = "abcd" and B = "cdabcdab". Return 3, because by repeating A three times (“abcdabcdabcd”),
B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").

Concatenate n copies of A until it is at least the length of B. If B is a substing of any number of copies of A it must
be a substring of the n copies or n + 1 copies, since n + 2 copies means there must be a whole unused copy of A.
Time - O(n**2) where n is the length of B.
Space - O(n)
*/

class Solution {
    public int repeatedStringMatch(String A, String B) {

        int n = 1;
        StringBuilder sb = new StringBuilder(A);
        while (sb.length() < B.length()) {
            sb.append(A);
            ++n;
        }

        if (sb.indexOf(B) != -1)
            return n;

        if (sb.append(A).indexOf(B) != -1)
            return n + 1;

        return -1;
    }
}
