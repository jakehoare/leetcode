/*
https://leetcode.com/problems/nim-game/
You are playing the following Nim Game with your friend: There is a heap of stones on the table, each time one of
you take turns to remove 1 to 3 stones. The one who removes the last stone will be the winner. You will take the
first turn to remove the stones.
Both of you are very clever and have optimal strategies for the game.
Write a function to determine whether you can win the game given the number of stones in the heap.

For 4 stones there is no winning strategy.  Likewise if the number of stones is a multiple of 4, the opponent can
always return it to a multiple of 4 after the first player's move.
Time - O(1)
Space - O(1)
*/


public class Solution {
    public boolean canWinNim(int n) {
        return n%4 != 0;
    }
}
