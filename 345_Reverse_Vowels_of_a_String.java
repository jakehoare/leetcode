/*
https://leetcode.com/problems/reverse-vowels-of-a-string/
Write a function that takes a string as input and reverse only the vowels of a string.

Use pointers to swap the first vowel on the left and right, then increment pointers inwards until overlap.
Time - O(n)
Space - O(n)
*/

public class Solution {
    public String reverseVowels(String s) {

        char[] sArray = s.toCharArray();
        Set<Character> vowels = new HashSet<Character>(Arrays.asList('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'));
        int left = 0;
        char temp;
        int right = s.length() - 1;

        while (left < right) {
            while (left < s.length() && !vowels.contains(s.charAt(left))) {
                left++;
            }
            while (right >= 0 && !vowels.contains(s.charAt(right))) {
                right--;
            }
            temp = s.charAt(left);
            sArray[left] = sArray[right];
            sArray[right] = temp;
            left++;
            right--;
        }

        return new String(sArray);

    }
}