/*
https://leetcode.com/problems/construct-the-rectangle/
Given a specific rectangular web page’s area, your job by now is to design a rectangular web page, whose length L and
width W satisfy the following requirements:
1. The area of the rectangular web page you designed must equal to the given target area.
2. The width W should not be larger than the length L, which means L >= W.
3. The difference between length L and width W should be as small as possible.
You need to output the length L and the width W of the web page you designed in sequence.

Width must be <= sqrt(area). Decrement width from this value until divides area.
Time - O(sqrt(n))
Space - O(1)
*/

public class Solution {
    public int[] constructRectangle(int area) {

        int width = (int) Math.sqrt(area);
        while (area % width != 0)
            --width;

        return new int[] {area / width,  width};
    }
}