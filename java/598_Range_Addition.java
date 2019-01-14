/*
https://leetcode.com/problems/range-addition-ii/
Given an m * n matrix M initialized with all 0's and several update operations.
Operations are represented by a 2D array, and each operation is represented by an array with two positive integers
a and b, which means M[i][j] should be added by one for all 0 <= i < a and 0 <= j < b.
You need to count and return the number of maximum integers in the matrix after performing all the operations.

Find minimum column and row that are updated.
Time - O(n)
Space - O(1)
*/

class Solution {
    public int maxCount(int m, int n, int[][] ops) {
        int sameRows = m;
        int sameCols = n;
        for (int[] op : ops) {
            sameRows = Math.min(sameRows, op[0]);
            sameCols = Math.min(sameCols, op[1]);
        }
        return sameRows * sameCols;
    }
}
