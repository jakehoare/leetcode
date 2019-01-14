/*
https://leetcode.com/problems/count-binary-substrings/
Give a string s, count the number of non-empty (contiguous) substrings that have the same number of 0's and 1's,
and all the 0's and all the 1's in these substrings are grouped consecutively.
Substrings that occur multiple times are counted the number of times they occur.

Iterate over string. When char is same as previous, increment count of current char and count of substrings if count
of current char <= count of previous previous char. Else if different char, updated prev count and increment substrings
unless first char of string.
Time - O(n)
Space - O(1)
*/

class Solution {
    public int countBinarySubstrings(String s) {

        int substrings = 0;
        int count = 0;
        int prevCount = 0;
        char prev = 'x';

        for (int i = 0; i < s.length(); ++ i) {

            if (s.charAt(i) == prev) {
                ++count;
                if (count <= prevCount)
                    ++substrings;
            } else {
                prev = s.charAt(i);
                prevCount = count;
                count = 1;
                if (prevCount > 0)  // always increment unless fisrt char of string
                    ++substrings;
            }

        }

        return substrings;
    }
}
