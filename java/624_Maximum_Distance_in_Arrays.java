/*
https://leetcode.com/problems/maximum-distance-in-arrays/
Given m arrays, and each array is sorted in ascending order. Now you can pick up two integers from two different
arrays (each array picks one) and calculate the distance. We define the distance between two integers a and b to be
their absolute difference |a-b|. Your task is to find the maximum distance.

Track the max an min values of all arrays seen. Update the distance if either the max from previous arrays - this
array min, or this array max - min from previous arrays is larger. The update max and min seen so far.
Time - O(n), number of arrays
Space - O(1)
*/

class Solution {
    public int maxDistance(List<List<Integer>> arrays) {
        int minVal = arrays.get(0).get(0);
        int maxVal = arrays.get(0).get(arrays.get(0).size() - 1);
        int maxDist = 0;

        for (int i = 1; i < arrays.size(); ++i) {
            int first = arrays.get(i).get(0);
            int last = arrays.get(i).get(arrays.get(i).size() - 1);
            maxDist = Math.max(maxDist, Math.abs(maxVal - first));
            maxDist = Math.max(maxDist, Math.abs(last - minVal));
            minVal = Math.min(minVal, first);
            maxVal = Math.max(maxVal, last);
        }
        return maxDist;
    }
}
