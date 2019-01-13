
/*
https://leetcode.com/problems/assign-cookies/
Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most
one cookie. Each child i has a greed factor gi, which is the minimum size of a cookie that the child will be content
with; and each cookie j has a size sj. If sj >= gi, we can assign the cookie j to the child i, and the child i will
be content. Your goal is to maximize the number of your content children and output the maximum number.

Sort children and cookies in ascending order. Iterate over cookies. If no more children, break. If child accepts cookie
then increment child and result count, else discard cookie. Greedy method, assign lowest values cookies to least greedy
chidren.
Time - O(n log n)
Space - O(1)
*/

public class Solution {
    public int findContentChildren(int[] g, int[] s) {

        Arrays.sort(g);
        Arrays.sort(s);
        int contented = 0;
        int child = 0;

        for (int cookie = 0; cookie < s.length; ++cookie) {
            if (child >= g.length)
                break;
            if (s[cookie] >= g[child]) {
                ++contented;
                ++child;
            }
        }

        return contented;
    }
}
