/*
https://leetcode.com/problems/number-of-boomerangs/
Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the
distance between i and j equals the distance between i and k (the order of the tuple matters).
Find the number of boomerangs.

For each point, find distances from each other points and count by distance. For each distance, boomerang from every
point at that distance to every other point.
Time - O(n**2)
Space - O(n)
*/

public class Solution {
    public int numberOfBoomerangs(int[][] points) {

        int boomerangs = 0;
        Map<Integer, Integer> distanceCounts = new HashMap<>();

        for (int i = 0; i < points.length; ++i) {
            for (int j = 0; j < points.length; ++j) {

                if (i == j)
                    continue;

                int dist = (points[i][0] - points[j][0]) * (points[i][0] - points[j][0]);
                dist += (points[i][1] - points[j][1]) * (points[i][1] - points[j][1]);

                distanceCounts.put(dist, distanceCounts.getOrDefault(dist, 0) + 1);
            }

            for (int count : distanceCounts.values())
                boomerangs += count * (count - 1);

            distanceCounts.clear();
        }

        return boomerangs;
    }
}