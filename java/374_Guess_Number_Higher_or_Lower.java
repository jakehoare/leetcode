/*
https://leetcode.com/problems/guess-number-higher-or-lower/
We are playing the Guess Game. The game is as follows:
I pick a number from 1 to n. You have to guess which number I picked.
Every time you guess wrong, I'll tell you whether the number is higher or lower.
You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):

Binary search.  Guess mid point of remaining range and return if correct else recurse higher or lower.
Time - O(log n)
Space - O(1)
*/

/* The guess API is defined in the parent class GuessGame.
   @param num, your guess
   @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
      int guess(int num); */

public class Solution extends GuessGame {
    public int guessNumber(int n) {
        int low = 1;
        int high = n;

        while (true) {
            int mid = low + (high - low) / 2;
            int g = guess(mid);
            if (g == 1)
                low = mid + 1;
            else if (g == -1)
                high = mid - 1;
            else
                return mid;
        }
    }
}
