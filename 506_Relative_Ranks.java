/*
https://leetcode.com/problems/relative-ranks/
Given scores of N athletes, find their relative ranks and the people with the top three highest scores, who will be
awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".

Copy nums and sort, then create a map from each num to its rank. For each num in original order, lookup rank in map.
Convert rank to medal.
Time - O(n log n)
Space - O(n)
*/

class Solution {
    public String[] findRelativeRanks(int[] nums) {

        int n = nums.length;
        String[] ranks = new String[n];
        Map<Integer, String> medals = new HashMap<Integer, String>();
        medals.put(1, "Gold Medal");
        medals.put(2, "Silver Medal");
        medals.put(3, "Bronze Medal");

        int[] numsCopy = nums.clone();
        Arrays.sort(numsCopy);
        Map<Integer, Integer> numToRank = new HashMap<Integer, Integer>();

        for (int i = 0; i < n; ++i)
            numToRank.put(numsCopy[i], n - i);

        int rank;
        for (int i = 0; i < n; ++i) {
            rank = numToRank.get(nums[i]);
            ranks[i] = medals.getOrDefault(rank, Integer.toString(rank));
        }

        return ranks;
    }
}