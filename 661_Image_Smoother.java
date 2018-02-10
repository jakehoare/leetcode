/*
https://leetcode.com/problems/image-smoother/
Given a 2D integer matrix M representing the gray scale of an image, you need to design a smoother to make the gray
scale of each cell becomes the average gray scale (rounding down) of all the 8 surrounding cells and itself. If a cell
has less than 8 surrounding cells, then use as many as you can.

Iterate over cells of image. For each cell count neighbours and sum their values. Set smoothed pixel to sum / count.
Time - O(mn)
Space - O(mn)
*/

class Solution {
    public int[][] imageSmoother(int[][] M) {

        int rows = M.length;
        int cols = M[0].length;
        int[][] smoothed = new int[rows][cols];

        for (int r = 0; r < rows; ++r) {
            for (int c = 0; c < cols; ++c) {

                int count = 0;
                int total = 0;
                for (int nr = r - 1; nr < r + 2; ++nr) {
                    for (int nc = c - 1; nc < c + 2; ++nc) {
                        if (nr < 0 || nr >= rows || nc < 0 || nc >= cols)
                            continue;
                        ++count;
                        total += M[nr][nc];
                    }
                }
                smoothed[r][c] = total / count;
            }
        }
        return smoothed;
    }
}