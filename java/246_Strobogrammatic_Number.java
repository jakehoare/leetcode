/*
https://leetcode.com/problems/strobogrammatic-number/
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
Write a function to determine if a number is strobogrammatic. The number is represented as a string.
For example, the numbers "69", "88", and "818" are all strobogrammatic.

If we find any character that cannot be inverted return false.  If any character at the inverted location
is not equal to the inverted original character then return false.
Time - O(n)
Space - O(1)
*/

public class Solution {
    public boolean isStrobogrammatic(String num) {

        HashMap<Character, Character> strobo = new HashMap<Character, Character>();
        strobo.put('0', '0');
        strobo.put('1', '1');
        strobo.put('8', '8');
        strobo.put('6', '9');
        strobo.put('9', '6');

        for (int i = 0; i < (num.length()+1) / 2; ++i) {

            char c = num.charAt(i);
            if (!strobo.containsKey(c)) {
                return false;
            }
            if (!strobo.get(c).equals(num.charAt(num.length()-1-i)))
                return false;
        }
        return true;
    }
}
