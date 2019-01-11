/*
https://leetcode.com/problems/third-maximum-number/
Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return
the maximum number.

Initialise top 3 maxima as null. If num is any of the maxima, continue. If not find the first samaller or null maximum.
Time - O(n)
Space - O(1)
*/

public class Solution {
    public int thirdMax(int[] nums) {

        Integer max1 = null;    // int cannot be null so use Integer
        Integer max2 = null;
        Integer max3 = null;

        for (Integer num : nums) {      // .equals() compares values, false if max3 is null
            if (num.equals(max3) || num.equals(max2) || num.equals(max1))
                continue;

            if (max1 == null || num > max1) {       // == compares references
                max3 = max2;                        // .equals() gives NullPointerException
                max2 = max1;
                max1 = num;
            } else if (max2 == null || num > max2) {
                max3 = max2;
                max2 = num;
            }
            else if (max3 == null || num > max3)
                max3 = num;
        }

        return max3 == null ? max1 : max3;

    }
}
