/*
https://leetcode.com/problems/find-smallest-letter-greater-than-target/
Given a list of sorted characters letters containing only lowercase letters, and given a target letter target, find
the smallest element in the list that is larger than the given target.
Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.

Binary search range of indices of next letter. If target >= guess then then search to the right of (and excluding) mid.
Else search left of and including mid.
Time - O(log n)
Space - O(1)
*/

class Solution {
    public char nextGreatestLetter(char[] letters, char target) {

        int left = 0;
        int right = letters.length;

        while (left < right) {

            int mid = (left + right) / 2;
            if (target >= letters[mid])
                left = mid + 1;
            else
                right = mid;
        }

        return letters[left % letters.length];
    }
}
