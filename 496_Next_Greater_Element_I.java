/*
https://leetcode.com/problems/next-greater-element-i/
You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. Find all the
next greater numbers for nums1's elements in the corresponding places of nums2.
The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not
exist, output -1 for this number.

Maintain a stack of nums seen thathav not found a greater element and is hence in decreasing order. For each num, pop
all off stack that are lower and record popped num and its next greater element in map. Push num to map.
Populate result by searching map for each num in findNums.
Time - O(n)
Space - O(n)
*/

public class Solution {
    public int[] nextGreaterElement(int[] findNums, int[] nums) {

        int[] result = new int[findNums.length];
        Stack<Integer> stack = new Stack<Integer>();      // decreasing sequence
        Map<Integer, Integer> numToGreater = new HashMap<Integer, Integer>();

        for (int num : nums) {
            while (!stack.isEmpty() && num > stack.peek())
                numToGreater.put(stack.pop(), num);
            stack.push(num);
        }

        for (int i = 0; i < findNums.length; ++i)
            result[i] = numToGreater.getOrDefault(findNums[i], -1);

        return result;
    }
}