/*
https://leetcode.com/problems/k-diff-pairs-in-an-array/
Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array. Here a
k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their absolute
difference is k.

Count frequencies. For each uniquie num, if k != 0 then increment pairs if num + k exists. If k == 0 then increment
pairs if more than one copy of num exists.
Time - O(n)
Space - O(n)
*/

class Solution {
    public int findPairs(int[] nums, int k) {

        if (k < 0)
            return 0;

        int pairs = 0;
        Map<Integer, Integer> freq = new HashMap<Integer, Integer>();
        for (int num : nums)
            freq.put(num, freq.getOrDefault(num, 0) + 1);

        for (int num : freq.keySet()) {
            if (k == 0) {
                if (freq.get(num) > 1)
                    ++pairs;
            } else if (freq.containsKey(num + k))
                ++pairs;
        }

        return pairs;
    }
}