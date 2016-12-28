/*
https://leetcode.com/problems/paint-fence/
There is a fence with n posts, each post can be painted with one of the k colors.
You have to paint all the posts such that no more than two adjacent fence posts have the same color.
n and k are non-negative integers.

For each post calculate the number of ways to paint it the same as previous and the number of ways to paint it
differently.  For each way that previous post was painted differently from its previous, we can paint current post
the same.  For each way to paint the previous post (either same or different) we can choose any other colour
and the current post is different.
Time - O(n)
Space - O(1)
*/


public class Solution {
    public int numWays(int n, int k) {
        if (k == 0 || n == 0)       // no ways to paint if no posts or colours
            return 0;

        int same = 0;               // base case of 1 post
        int different = k;

        for (int post = 1; post < n; ++post) {
            int temp = same;
            same = different;
            different = (k-1) * (temp + different);
        }

        return same + different;
    }
}