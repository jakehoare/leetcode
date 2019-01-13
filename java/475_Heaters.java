/*
https://leetcode.com/problems/heaters/
Winter is coming! Your first job during the contest is to design a standard heater with fixed warm radius to warm
all the houses. You are given positions of houses and heaters on a horizontal line, find out minimum radius of heaters
so that all houses could be covered by those heaters.
Your input will be the positions of houses and heaters seperately, and your expected output will be the minimum radius
standard of heaters.
As long as a house is in the heaters' warm radius range, it can be warmed.
All the heaters follow your radius standard and the warm radius will the same.

Sort the houses and heaters in ascending order. For each house, if the next heater is the same distance or closer,
increment the current heater. Then the best closest heater is found, update the minRadius.
Time - O(mlogm + nlogn)
Space - O(m + n)
*/

public class Solution {
    public int findRadius(int[] houses, int[] heaters) {
        Arrays.sort(houses);
        Arrays.sort(heaters);

        int minRadius = 0;
        int j = 0;              // heater index
        int distance = 0;       // between current house and current heater

        for (int house : houses) {
            distance = Math.abs(house - heaters[j]);
            while (j < heaters.length - 1 && Math.abs(house - heaters[j + 1]) <= distance) {
                distance = Math.abs(house - heaters[j + 1]);
                ++j;
            }
            minRadius = Math.max(minRadius, distance);
        }

        return minRadius;
    }
}
