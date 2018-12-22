/*
https://leetcode.com/problems/intersection-of-two-arrays-ii/
Given two arrays, write a function to compute their intersection.
Each element in the result should appear as many times as it shows in both arrays.

Count the frequencies in one array.  For each element in other array, if it has a positive count then add to result and
decrement count.
Time - O(m + n)
Space - O(m), count map is size of first array so preferable to count the array with fewer distinct elements.
*/

public class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {

        HashMap<Integer, Integer> count = new HashMap<Integer, Integer>();
        ArrayList<Integer> result = new ArrayList<Integer>();

        for (int n : nums1) {
            if(map.containsKey(n)
                map.put(n, map.get(n) + 1);
            else map.put(n, 1);
        }

        for(int n : nums2) {
            if(map.containsKey(n) && map.get(n) > 0)
            {
                result.add(n);
                map.put(n, map.get(n) - 1);
            }
        }

       int[] res = new int[result.size()];
       for (int i = 0; i < result.size(); i++) {
           res[i] = result.get(i);
       }

       return res;
    }
}
