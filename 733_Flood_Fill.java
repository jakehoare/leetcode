/*
https://leetcode.com/problems/flood-fill/
An image is represented by a 2-D array of integers, each integer representing the pixel value of the image
(from 0 to 65535).
Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value
newColor, "flood fill" the image.
To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel
of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same
color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.
At the end, return the modified image.

Depth first search. If newColor is same as first pixel then return to avoid an infinite loop. Else if a pixel is
startColor then change it to newColor and recurse for all neighbours.
Time - O(mn)
Space - O(1)
*/

class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int newColor) {

        int startColor = image[sr][sc];
        if (startColor == newColor)         // avoid infinite loop
            return image;

        helper(image, sr, sc, newColor, startColor);
        return image;
    }

    private void helper(int[][] image, int sr, int sc, int newColor, int startColor) {

        if (sr < 0 || sc < 0 || sr >= image.length || sc >= image[0].length)
            return;

        if (image[sr][sc] != startColor)
            return;

        image[sr][sc] = newColor;
        helper(image, sr + 1, sc, newColor, startColor);
        helper(image, sr - 1, sc, newColor, startColor);
        helper(image, sr, sc + 1, newColor, startColor);
        helper(image, sr, sc - 1, newColor, startColor);
    }
}