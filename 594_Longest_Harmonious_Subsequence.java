/*
https://leetcode.com/problems/longest-harmonious-subsequence/
We define a harmonious array is an array where the difference between its maximum value and its minimum value
is exactly 1. Now, given an integer array, you need to find the length of its longest harmonious subsequence among
all its possible subsequences.

Count the frequency of each num. Then for each num, if the count of num + 1 is not zero then there is a harmonious
subsequence containing num and num + 1.
Time - O(n)
Space - O(n)
*/

class Solution {
    public int findLHS(int[] nums) {

        int longest = 0;
        Map<Integer, Integer> freq = new HashMap<>();

        for (int num : nums)
            freq.put(num, freq.getOrDefault(num, 0) + 1);

        for (Map.Entry<Integer, Integer> entry : freq.entrySet()) {
            int higherCount = freq.getOrDefault(entry.getKey() + 1, 0);
            if (higherCount != 0)
                longest = Math.max(longest, entry.getValue() + higherCount);
        }

        return longest;
    }
}