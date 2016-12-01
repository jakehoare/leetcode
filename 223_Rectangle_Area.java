/*
https://leetcode.com/problems/rectangle-area/
Find the total area covered by two rectilinear rectangles in a 2D plane.
Each rectangle is defined by its bottom left corner and top right corner.

Calculate left, right, top, bottom edges of overlap.  If inverted then no overlap, else subtract
overlap area from sum of rectangles.
Time - O(1)
Space - O(1)
 */

public class Solution {
    public int computeArea(int A, int B, int C, int D, int E, int F, int G, int H) {

        int right_edge = Math.min(C, G);
        int left_edge = Math.max(A, E);

        int top_edge = Math.min(D, H);
        int bottom_edge = Math.max(B, F);

        int overlap = 0;
        if (right_edge > left_edge && top_edge > bottom_edge)
            overlap = (right_edge - left_edge) * (top_edge - bottom_edge);

        int r1 = (C-A) * (D-B);
        int r2 = (G-E) * (H-F);

        return r1 + r2 - overlap;
    }
}