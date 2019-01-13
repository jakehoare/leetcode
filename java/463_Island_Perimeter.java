/*
https://leetcode.com/problems/island-perimeter/
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid
cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there
is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that
isn't connected to the water around the island). One cell is a square with side length 1.
Determine the perimeter of the island.

Iterate over grid. Land squares have 4 borders with water by default. If a cell has land to the left, reduce the
number of perimeters by 2. Likewise for land above.
Time - O(mn)
Space - O(1)
*/

public class Solution {
    public int islandPerimeter(int[][] grid) {

        int perimeter = 0;

        for (int row = 0; row < grid.length; ++row) {
            for (int col = 0; col < grid[0].length; ++col) {

                if (grid[row][col] == 1) {      // ignore if cell is blank
                    perimeter += 4;
                    if (row != 0 && grid[row - 1][col] == 1)
                        perimeter -= 2;
                    if (col != 0 && grid[row][col - 1] == 1)
                        perimeter -= 2;
                }
            }
        }

        return perimeter;
    }
}
