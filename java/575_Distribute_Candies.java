/*
https://leetcode.com/problems/distribute-candies/
Given an integer array with even length, where different numbers in this array represent different kinds of candies.
Each number means one candy of the corresponding kind. You need to distribute these candies equally in number to
brother and sister. Return the maximum number of kinds of candies the sister could gain.

Count number of unique candies with set. Return lower of unique candies and number of candies each child gets.
Time - O(n)
Space - O(n)
*/

class Solution {
    public int distributeCandies(int[] candies) {
        Set<Integer> set = new HashSet<>();
        for (int c : candies) {
            set.add(c);
        }
        return Math.min(candies.length / 2, set.size());
    }
}
