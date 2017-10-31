/*
https://leetcode.com/problems/can-place-flowers/
Suppose you have a long flowerbed in which some of the plots are planted and some are not.
However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.
Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a
number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.

Iterate over flowerbed, moving forward to the next potentially free space if there is a flower in a cell or and
adjacent cells. Wehne flower can be planted, decrement count still to plant and test if count is zero.
Time - O(n)
Space - O(1)
*/

class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {

        if (n == 0)
            return true;

        int i = 0;
        while (i < flowerbed.length) {

            if (i != flowerbed.length - 1 && flowerbed[i + 1] == 1)
                i += 3;
            else if (flowerbed[i] == 1)
                i += 2;
            else if (i != 0 && flowerbed[i - 1] == 1)
                i += 1;
            else {      // place flower at flowerbed[i]
                --n;
                if (n == 0)
                    return true;
                i += 2;
            }
        }
        return false;
    }
}