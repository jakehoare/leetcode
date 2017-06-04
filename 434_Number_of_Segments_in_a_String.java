/*
https://leetcode.com/problems/number-of-segments-in-a-string/
Count the number of segments in a string, where a segment is defined to be a contiguous sequence of
non-space characters. Note that the string does not contain any non-printable characters.

Iterate over characters. Boolean blank indicates if previous char was whitespace. If blank and char is not whitespace
we have a new segment and blank is false. If whitespace, blank is true.
Time - O(n)
Space - O(1)
*/

public class Solution {
    public int countSegments(String s) {

        int segments = 0;
        boolean blank = true;

        for (int i = 0; i < s.length(); ++i) {

            if (blank && !Character.isWhitespace(s.charAt(i))) {
                ++segments;
                blank = false;
            }
            else if (Character.isWhitespace(s.charAt(i)))
                blank = true;

        }
        return segments;
    }
}