/*
https://leetcode.com/problems/minimum-index-sum-of-two-lists/
Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants
represented by strings.
You need to help them find out their common interest with the least list index sum. If there is a choice tie between
answers, output all of them with no order requirement. You could assume there always exists an answer.
No duplicates in both lists.

Map each string in the first list to its index. For each string in the second list, if it is in the first list then
calculate sun if indices. If better than previous best start a new results list, else append to results.
Time - O(m + n)
Space - O(m)
*/

class Solution {
    public String[] findRestaurant(String[] list1, String[] list2) {

        int minSum = list1.length + list2.length;
        List<String> result = new LinkedList<>();
        Map<String, Integer> map = new HashMap<>();

        for (int i = 0; i < list1.length; ++i)
                map.put(list1[i], i);               // lists have no duplicates

        for (int j = 0; j < list2.length; ++j) {
            if (map.get(list2[j]) != null) {
                int sum = j + map.get(list2[j]);
                if (sum <= minSum) {
                    if (sum < minSum) {
                        minSum = sum;
                        result = new LinkedList<>();
                    }
                    result.add(list2[j]);
                }
            }
        }

        return result.toArray(new String[result.size()]);
    }
}