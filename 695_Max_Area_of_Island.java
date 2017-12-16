/*
https://leetcode.com/problems/max-area-of-island/
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected
4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

DFS to get area of each island. Set visited cells to zero.
Time - O(mn)
Space - O(mn)
*/

class Solution {

    int[][] grid;
    int rows;
    int cols;

    public int maxAreaOfIsland(int[][] grid) {
        this.grid = grid;
        int maxArea = 0;
        this.rows = grid.length;
        this.cols = grid[0].length;
        if (this.rows == 0 || this.cols == 0)
            return 0;

        for (int r = 0; r < this.rows; ++r)
            for (int c = 0; c < this.cols; ++c)
                maxArea = Math.max(maxArea, getArea(r, c));

        return maxArea;
    }

    private int getArea(int r, int c) {
        if (r < 0 || r >= this.rows || c < 0 || c >= this.cols)
            return 0;
        if (grid[r][c] == 0)
            return 0;

        grid[r][c] = 0;
        return 1 + getArea(r + 1, c) + getArea(r - 1, c) +
            getArea(r, c + 1) + getArea(r, c - 1);
    }
}