/*
https://leetcode.com/problems/minimum-moves-to-equal-array-elements/
Given a non-empty integer array of size n, find the minimum number of moves required to make all array elements equal,
where a move is incrementing n - 1 elements by 1.

Incrementing n-1 elements is equivalent to decrementing one element. All elements must nbe decrement to the minimum.
Time - O(n)
Space - O(1)
*/

public class Solution {
    public int minMoves(int[] nums) {

        int moves = 0;
        int minimum = Integer.MAX_VALUE;

        for (int num : nums) {
            moves += num;
            minimum = Math.min(minimum, num);
        }

        return sum - (minimum * nums.length);
    }
}
