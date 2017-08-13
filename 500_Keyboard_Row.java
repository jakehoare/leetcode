/*
https://leetcode.com/problems/keyboard-row/
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of a keyboard.

Create a map of lower case letter to their rows. For each word, convert chars to lower case and check all rows are
same as for first char.
Time - O(n), total length of all words
Space - O(1)
*/

public class Solution {
    public String[] findWords(String[] words) {
        Map<Character, Integer> charToRow = new HashMap<Character, Integer>();
        String row1 = "qwertyuiop";
        String row2 = "asdfghjkl";
        String row3 = "zxcvbnm";
        for (int i = 0; i < row1.length(); ++i)
            charToRow.put(row1.charAt(i), 1);
        for (int i = 0; i < row2.length(); ++i)
            charToRow.put(row2.charAt(i), 2);
        for (int i = 0; i < row3.length(); ++i)
            charToRow.put(row3.charAt(i), 3);

        List<String> singleRow = new ArrayList<String>();
        for (String s : words) {
            if (s.length() == 0)
                continue;
            int row = charToRow.get(Character.toLowerCase(s.charAt(0)));
            for (int i = 1; i < s.length(); ++i) {
                if (charToRow.get(Character.toLowerCase(s.charAt(i))) != row) {
                    row = 0;    // flags that not all rows are same
                    break;
                }
            }
            if (row != 0)
                singleRow.add(s);
        }

        return singleRow.toArray(new String[singleRow.size()]);
    }
}