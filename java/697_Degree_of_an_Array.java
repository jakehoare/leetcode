/*
https://leetcode.com/problems/degree-of-an-array/
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency
of any one of its elements.
Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Use 3 hashmaps to store the count, first and last indices of each num. Then find the most frequent num, breaking ties
by shortest distance between first and last.
Time - O(n)
Space - O(n)
*/

class Solution {
    public int findShortestSubArray(int[] nums) {

        HashMap<Integer, Integer> counts = new HashMap<>();     // map num to its count
        HashMap<Integer, Integer> first = new HashMap<>();      // map num to its first index
        HashMap<Integer, Integer> last = new HashMap<>();       // map num to its last index

        for (int i = 0; i < nums.length; ++i) {

            int count = counts.getOrDefault(nums[i], 0);
            if (count == 0)
                first.put(nums[i], i);

            last.put(nums[i], i);
            counts.put(nums[i], count + 1);
        }

        int shortest = nums.length;
        int mostFrequent = 0;

        for (Map.Entry<Integer, Integer> entry : counts.entrySet()) {

            int num = entry.getKey();
            int count = entry.getValue();
            int distance = last.get(num) - first.get(num) + 1;

            if (count > mostFrequent || count == mostFrequent && distance < shortest) {
                shortest = distance;
                mostFrequent = count;
            }

        }

        return shortest;
    }
}
