/*
https://leetcode.com/problems/reshape-the-matrix/
In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different
size but keep its original data.
You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the row
number and column number of the wanted reshaped matrix, respectively.
The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order
as they were.
If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix;
Otherwise, output the original matrix.

Test if number of elements in new matrix matches old. Create empty new matrix. Iterate over old matrix, moving pointer
along row of new matrix and incrementing row at end of column.
Time - O(m * n)
Space - O(m * n)
*/

class Solution {
    public int[][] matrixReshape(int[][] nums, int r, int c) {

        int old_r = nums.length;        // guaranteed not to be null
        int old_c = nums[0].length;

        if (old_r * old_c != r * c)
            return nums;

        int[][] result = new int[r][c];
        int m = 0;  // row index in result
        int n = 0;  // col index in result;

        for (int i = 0; i < old_r; ++i) {
            for (int j = 0; j < old_c; ++j) {
                result[m][n++] = nums[i][j];
                if (n >= c) {
                    n = 0;
                    ++m;
                }
            }
        }

        return result;
    }
}